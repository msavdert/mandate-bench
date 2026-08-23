#!/usr/bin/env python3
"""Bootstrap confidence intervals for Experiment 1 dispersion figures.

Usage: python3 harness/bootstrap_ci.py [results_dir] [snapshot.json]

Regenerates the bootstrap 95% CIs quoted in RESULTS.md's "Dispersion
ranking" table and in the S3 verdict (the Kimi-K3 vs Gemini 3.7 Flash
dispersion ratio). The resampling unit is the RUN: for each model, draw
N runs with replacement from that model's usable runs (N = number of
usable runs for that model) and recompute mean pairwise distance (MPD)
on the resampled set, exactly as analyze.py computes it on the original
set. Repeat `--resamples` times and report the 2.5th/97.5th percentiles
of the resulting distribution (a percentile bootstrap).

For the cross-model ratio, each resample iteration independently
resamples every model's runs, recomputes each model's MPD, and takes
max(MPD)/min(MPD) across models for that iteration; the CI is the
2.5/97.5 percentile of that ratio distribution.

This script reuses analyze.py's run-loading and MPD code directly
(analyze_model, mean_pairwise_distance) for point estimates and for the
distance metric itself, rather than reimplementing parsing or the
distance formula. For the resampling loop it precomputes each model's
n x n pairwise-distance matrix once (using that same 0.5 * sum |delta|
formula) and then, per resample, looks up cached distances by drawn
index instead of recomputing weight deltas from scratch -- otherwise
10000 resamples x 6 models x C(50,2) pairs x 11 assets of pure-Python
dict arithmetic takes several minutes. The cache makes the two
computations equivalent (same formula, same inputs) but the resampling
loop tens of times faster.

Standard library only. Deterministic given --seed (default 42, matching
the seed RESULTS.md cites for the published ratio CI). Default
--resamples is 2000, which completes in well under a minute at these
sample sizes (n<=50 runs/model) and is plenty for a stable 95%
percentile CI; pass a larger value (e.g. 10000) for a smoother estimate
if you have the time.

Reproduction note (see VERIFY step in the commit that added this
script): with --resamples 2000 --seed 42 (and also checked at 10000),
this script reproduces the published per-model MPD point estimates in
RESULTS.md's "Dispersion ranking" table (6.27, 4.98, 3.85, 3.65, 3.11,
2.31) exactly, and reproduces the S3 ratio point estimate (2.71x)
exactly. The bootstrap CIs it computes are close to but not bit-for-bit
identical to the published CIs (different RNG stream/resample count
than whatever produced the original numbers, which is expected for a
Monte Carlo estimate) -- see the script's own printed output for the
current values and compare by eye against RESULTS.md.
"""

import argparse
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyze import (  # noqa: E402
    ALL_ASSETS,
    analyze_model,
    mean_pairwise_distance,
)

# Experiment 1's six models (results/claude-opus is a later, separate arm
# and results/judge holds no run_*.json files; both are excluded here).
# Display names match RESULTS.md's "Dispersion ranking" table.
DISPLAY_NAMES = {
    "synthetic-syn-large-vision-high": "Kimi-K3 (syn:large:vision)",
    "synthetic-syn-small-vision-high": "Qwen3.6-27B (syn:small:vision)",
    "claude-sonnet": "Claude Sonnet 5 (claude -p)",
    "google-antigravity-gemini-3.1-pro-high": "Gemini 3.1 Pro high",
    "synthetic-syn-large-text-high": "GLM-5.2 (syn:large:text)",
    "google-antigravity-gemini-3.7-flash-high": "Gemini 3.7 Flash high",
}


def percentile(sorted_values, pct):
    """Nearest-rank-interpolated percentile on an already-sorted list,
    pct in [0, 100]."""
    if not sorted_values:
        return None
    k = (len(sorted_values) - 1) * (pct / 100.0)
    lo = int(k)
    hi = min(lo + 1, len(sorted_values) - 1)
    frac = k - lo
    return sorted_values[lo] + (sorted_values[hi] - sorted_values[lo]) * frac


def pairwise_distance(wi, wj):
    """Same distance formula as analyze.mean_pairwise_distance's inner loop."""
    return 0.5 * sum(abs(wi[a] - wj[a]) for a in ALL_ASSETS)


def build_distance_matrix(records):
    """n x n matrix of pairwise distances between records' weights (0 on
    the diagonal), using the same formula analyze.mean_pairwise_distance
    uses. Precomputed once per model so the bootstrap loop can look up
    distances instead of recomputing them on every resample."""
    n = len(records)
    weights = [r["weights"] for r in records]
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = pairwise_distance(weights[i], weights[j])
            matrix[i][j] = d
            matrix[j][i] = d
    return matrix


def resample_mpd_from_matrix(matrix, n, rng):
    """Draw n indices with replacement and compute mean pairwise distance
    over the resampled set using the cached distance matrix. Equivalent
    to calling analyze.mean_pairwise_distance on the resampled records,
    but avoids recomputing weight deltas."""
    if n < 2:
        return None
    idx = [rng.randrange(n) for _ in range(n)]
    total = 0.0
    count = 0
    for a in range(n):
        ia = idx[a]
        row = matrix[ia]
        for b in range(a + 1, n):
            total += row[idx[b]]
            count += 1
    return total / count if count else None


def bootstrap_model_ci(matrix, n, resamples, rng):
    values = []
    for _ in range(resamples):
        mpd = resample_mpd_from_matrix(matrix, n, rng)
        if mpd is not None:
            values.append(mpd)
    values.sort()
    return percentile(values, 2.5), percentile(values, 97.5)


def bootstrap_ratio_ci(model_matrices, resamples, rng):
    """model_matrices: dict dir_name -> (matrix, n). Returns (lo, hi) for
    the max(MPD)/min(MPD) ratio across models, resampled independently
    per model at each iteration."""
    ratios = []
    for _ in range(resamples):
        mpds = {}
        for name, (matrix, n) in model_matrices.items():
            mpd = resample_mpd_from_matrix(matrix, n, rng)
            if mpd is not None:
                mpds[name] = mpd
        if len(mpds) < 2 or min(mpds.values()) <= 0:
            continue
        ratios.append(max(mpds.values()) / min(mpds.values()))
    ratios.sort()
    return percentile(ratios, 2.5), percentile(ratios, 97.5)


def fmt(x, decimals=2):
    return "n/a" if x is None else f"{x:.{decimals}f}"


def main():
    parser = argparse.ArgumentParser(
        description="Bootstrap 95%% CIs for Experiment 1 dispersion (MPD) figures."
    )
    parser.add_argument(
        "results_dir", nargs="?", default=str(ROOT / "results"),
        help="Directory containing per-model run_*.json/.txt subfolders (default: results/)",
    )
    parser.add_argument(
        "snapshot", nargs="?", default=str(ROOT / "data" / "snapshot.json"),
        help="Path to snapshot.json with current_portfolio (default: data/snapshot.json)",
    )
    parser.add_argument(
        "--resamples", type=int, default=2000,
        help="Number of bootstrap resamples per model/ratio (default: 2000)",
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="Random seed for reproducibility (default: 42)",
    )
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    snapshot_path = Path(args.snapshot)

    if not snapshot_path.exists():
        print(f"ERROR: {snapshot_path} not found; run fetch_data.py first", file=sys.stderr)
        sys.exit(1)
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    current_portfolio = {a: float(v) for a, v in snapshot["current_portfolio"].items()}

    model_records = {}
    for dir_name in DISPLAY_NAMES:
        model_dir = results_dir / dir_name
        if not model_dir.is_dir():
            print(f"WARNING: {model_dir} not found, skipping", file=sys.stderr)
            continue
        records, _total_files = analyze_model(model_dir, current_portfolio)
        model_records[dir_name] = records

    rng = random.Random(args.seed)

    print(f"# Bootstrap 95% CIs (resamples={args.resamples}, seed={args.seed})")
    print()
    print("| Model | n | MPD | 95% CI |")
    print("|---|---|---|---|")

    point_mpds = {}
    model_matrices = {}
    for dir_name in DISPLAY_NAMES:
        records = model_records.get(dir_name)
        if not records:
            continue
        n = len(records)
        point = mean_pairwise_distance(records)
        point_mpds[dir_name] = point
        matrix = build_distance_matrix(records)
        model_matrices[dir_name] = (matrix, n)
        lo, hi = bootstrap_model_ci(matrix, n, args.resamples, rng)
        print(
            f"| {DISPLAY_NAMES[dir_name]} | {n} | {fmt(point)} | "
            f"{fmt(lo)}-{fmt(hi)} |"
        )

    print()
    if len(point_mpds) >= 2:
        max_name = max(point_mpds, key=point_mpds.get)
        min_name = min(point_mpds, key=point_mpds.get)
        point_ratio = point_mpds[max_name] / point_mpds[min_name]
        lo, hi = bootstrap_ratio_ci(model_matrices, args.resamples, rng)
        print(
            f"Cross-model ratio ({DISPLAY_NAMES[max_name]} / "
            f"{DISPLAY_NAMES[min_name]}): {fmt(point_ratio)}x, "
            f"bootstrap 95% CI [{fmt(lo)}, {fmt(hi)}]"
        )


if __name__ == "__main__":
    main()
