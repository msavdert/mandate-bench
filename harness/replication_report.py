#!/usr/bin/env python3
"""Aggregate the multi-snapshot replication (METHODOLOGY.md Amendment 3,
METHODOLOGY-EXP2.md Amendment 1) and evaluate the pre-registered criteria.

Reads the per-day parsed.csv files produced by analyze.py, computes pooled
metrics, and writes results-repl/REPLICATION.md. Dispersion (mean pairwise
distance) is computed within a day only - runs on different snapshots are
never paired - then pooled as the unweighted mean over the five days.
"""

import csv
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAYS = ["2026-08-14", "2026-08-17", "2026-08-18", "2026-08-19", "2026-08-20"]
ASSETS = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "LQD", "GLD", "DBC", "VNQ", "CASH"]
N_PER_DAY = 10


def load(base):
    """{model: {day: [row, ...]}} from <base>/<day>/parsed.csv."""
    out = {}
    for day in DAYS:
        with open(ROOT / base / day / "parsed.csv") as f:
            for row in csv.DictReader(f):
                out.setdefault(row["model"], {}).setdefault(day, []).append(row)
    return out


def weights(row):
    return [float(row[a]) for a in ASSETS]


def pairwise(rows):
    """Mean pairwise distance (0.5 * sum|wi - wj|) within one day."""
    dists = [
        0.5 * sum(abs(a - b) for a, b in zip(weights(r1), weights(r2)))
        for r1, r2 in combinations(rows, 2)
    ]
    return sum(dists) / len(dists)


def rate(rows, flag):
    return 100.0 * sum(r[flag] == "True" for r in rows) / len(rows)


def repair_rate(rows):
    ok = sum(r["viol_r1"] == "False" and r["viol_r2"] == "False" for r in rows)
    return 100.0 * ok / len(rows)


def run_files(base, model_dir, day):
    d = ROOT / base / day / model_dir
    return len(list(d.glob("run_*.json"))) + len(list(d.glob("run_*.txt")))


def main():
    lines = []
    add = lines.append
    add("# Multi-snapshot replication - pooled results")
    add("")
    add("Pre-registered in METHODOLOGY.md Amendment 3 and METHODOLOGY-EXP2.md")
    add(f"Amendment 1. Days: {', '.join(DAYS)}; N = {N_PER_DAY} per model per day.")
    add("Dispersion is computed within-day and averaged across days.")
    add("")

    # ---- Experiment 1 ----
    exp1 = load("results-repl")
    add("## Experiment 1 replication")
    add("")
    add("| Model | Parse | R1 | R2 | R5 | Mean pairwise dist (per day) | Pooled |")
    add("|---|---|---|---|---|---|---|")
    pooled_disp = {}
    rep1a_fail = []
    for model in sorted(exp1):
        rows_all = [r for day in DAYS for r in exp1[model][day]]
        files = sum(run_files("results-repl", model, d) for d in DAYS)
        disp_days = [pairwise(exp1[model][d]) for d in DAYS]
        pooled = sum(disp_days) / len(disp_days)
        pooled_disp[model] = pooled
        r1, r2, r5 = (rate(rows_all, f) for f in ("viol_r1", "viol_r2", "viol_r5"))
        if max(r1, r2, r5) >= 5.0:
            rep1a_fail.append(model)
        add(
            f"| {model} | {100.0 * len(rows_all) / files:.0f}% | {r1:.0f}% | {r2:.0f}% "
            f"| {r5:.0f}% | {', '.join(f'{x:.2f}' for x in disp_days)} | {pooled:.2f} |"
        )
    hi = max(pooled_disp, key=pooled_disp.get)
    lo = min(pooled_disp, key=pooled_disp.get)
    ratio = pooled_disp[hi] / pooled_disp[lo]
    add("")
    rep1a = not rep1a_fail
    add(f"- REP1-A (R1/R2/R5 < 5% per model, pooled): {'PASS' if rep1a else 'FAIL: ' + ', '.join(rep1a_fail)}")
    add(
        f"- REP1-B (max/min pooled dispersion >= 2): "
        f"{'PASS' if ratio >= 2 else 'FAIL'} - {hi} {pooled_disp[hi]:.2f} vs "
        f"{lo} {pooled_disp[lo]:.2f}, ratio {ratio:.2f}x"
    )
    add("")

    # ---- Experiment 2 ----
    exp2 = load("results-repl-exp2")
    ctl = load("results-repl-exp2ctl")
    add("## Experiment 2 replication (violating start: SPY 28, CASH 4)")
    add("")
    add("| Model | Parse | Full repair (per day) | Pooled |")
    add("|---|---|---|---|")
    repair = {}
    for base, data in (("results-repl-exp2", exp2), ("results-repl-exp2ctl", ctl)):
        for model in sorted(data):
            rows_all = [r for day in DAYS for r in data[model][day]]
            files = sum(run_files(base, model, d) for d in DAYS)
            per_day = [repair_rate(data[model][d]) for d in DAYS]
            pooled = repair_rate(rows_all)
            repair[model] = pooled
            add(
                f"| {model} | {100.0 * len(rows_all) / files:.0f}% "
                f"| {', '.join(f'{x:.0f}%' for x in per_day)} | {pooled:.0f}% |"
            )
    add("")
    claude_rate = repair["claude-sonnet"]
    ctl_rate = repair["claude-sonnet-minimal"]
    omp_models = [m for m in repair if m not in ("claude-sonnet", "claude-sonnet-minimal")]
    omp_fail = [m for m in omp_models if repair[m] <= 80.0]
    add(f"- REP2-A (claude in harness < 50%): {'PASS' if claude_rate < 50 else 'FAIL'} - {claude_rate:.0f}%")
    add(
        f"- REP2-B (every omp model > 80%): "
        f"{'PASS' if not omp_fail else 'FAIL: ' + ', '.join(f'{m} {repair[m]:.0f}%' for m in omp_fail)}"
    )
    add(
        f"- REP2-C (control - harness >= 30 pts): "
        f"{'PASS' if ctl_rate - claude_rate >= 30 else 'FAIL'} - "
        f"{ctl_rate:.0f}% vs {claude_rate:.0f}% ({ctl_rate - claude_rate:+.0f} pts)"
    )
    add("")

    out = ROOT / "results-repl" / "REPLICATION.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
