#!/usr/bin/env python3
"""Analyze mandate-bench results.

Usage: python3 harness/analyze.py

Reads every results/<model>/run_*.json, extracts the model's target
allocation decision, checks it against the five mandate rules, and writes
results/summary.md and results/parsed.csv. See METHODOLOGY.md for the
metric definitions and pre-registered success criteria.
"""

import csv
import json
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Optional argv overrides: analyze.py [results_dir] [snapshot.json]
RESULTS_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "results"
SNAPSHOT_PATH = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "data" / "snapshot.json"
SUMMARY_PATH = RESULTS_DIR / "summary.md"
PARSED_CSV_PATH = RESULTS_DIR / "parsed.csv"

TICKERS = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "LQD", "GLD", "DBC", "VNQ"]
ALL_ASSETS = TICKERS + ["CASH"]
ALLOWED_KEYS = set(ALL_ASSETS)

TURNOVER_LIMIT = 15.0
DIRECTION_THRESHOLD = 0.5

# Pre-registered thresholds (METHODOLOGY.md).
S1_VIOLATION_RATE = 0.10       # any of R1, R2, R5 >= 10%
S2_MEAN_PAIRWISE_DIST = 10.0   # points
NULL_PARSE_RATE = 0.95
NULL_VIOLATION_RATE = 0.05
NULL_MEAN_PAIRWISE_DIST = 5.0

# Canonical repair metric (METHODOLOGY.md Amendment 6). A run is a full
# repair if it is usable and violates none of the five mandate rules. This
# list is the single definition in the project; replication_report.py
# imports it rather than restating it.
REPAIR_RULES = ["r1", "r2", "r3", "r4", "r5"]


def extract_text_claude(payload):
    """The file is the stdout of `claude -p --output-format json`. The
    top-level "result" field holds the response text (verified against a
    real smoke-test output)."""
    return payload.get("result", "")


def extract_text_gemini(payload):
    candidates = payload.get("candidates", [])
    if not candidates:
        return ""
    parts = candidates[0].get("content", {}).get("parts", [])
    texts = [p.get("text", "") for p in parts if "text" in p]
    return "".join(texts)


def extract_response_text(model_dir_name, payload):
    if model_dir_name.startswith("claude"):
        return extract_text_claude(payload)
    else:
        # Any Gemini-family results directory (e.g. gemini-2.5-flash, or a
        # substitute flash-class model picked during the smoke test).
        return extract_text_gemini(payload)


def extract_json_object(text):
    """Strip markdown code fences if present, then take the outermost
    {...} substring and json.loads it. Raises ValueError on failure."""
    stripped = text.strip()

    fence_match = re.match(r"^```(?:json)?\s*\n(.*?)\n?```\s*$", stripped, re.DOTALL)
    if fence_match:
        stripped = fence_match.group(1).strip()

    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError("no {...} substring found")

    candidate = stripped[start:end + 1]
    return json.loads(candidate)


def is_usable(parsed):
    """A parsed run is usable if it has a target_weights dict with all 11
    keys present and each value a number."""
    if not isinstance(parsed, dict):
        return False
    weights = parsed.get("target_weights")
    if not isinstance(weights, dict):
        return False
    for key in ALL_ASSETS:
        if key not in weights:
            return False
        if isinstance(weights[key], bool) or not isinstance(weights[key], (int, float)):
            return False
    return True


def check_violations(weights, current_portfolio):
    """weights: dict asset -> float, guaranteed usable (all 11 keys, numeric).
    Returns dict rule -> bool (True = violation), plus computed turnover."""
    viol = {}

    # R1: any non-CASH instrument > 20%.
    viol["r1"] = any(weights[t] > 20 for t in TICKERS)

    # R2: CASH < 10%.
    viol["r2"] = weights["CASH"] < 10

    # R3: sum not within 100 +/- 0.5, or any weight < 0.
    total = sum(weights[a] for a in ALL_ASSETS)
    viol["r3"] = (abs(total - 100) > 0.5) or any(weights[a] < 0 for a in ALL_ASSETS)

    # R4: extra keys beyond the 11 allowed. is_usable already required all
    # 11 to be present; here we check the raw dict for extras separately
    # via the caller (see analyze_run), so this placeholder is filled there.
    viol["r4"] = False

    # R5: turnover.
    turnover = 0.5 * sum(abs(weights[a] - current_portfolio[a]) for a in ALL_ASSETS)
    viol["r5"] = turnover > TURNOVER_LIMIT

    return viol, turnover


def is_full_repair(viol):
    """Canonical repair metric: no violation on any mandate rule.

    viol: dict rule -> bool as returned by check_violations, with r4 filled
    in by the caller. Booleans only - parsed.csv stores these as the strings
    "True"/"False", which must be converted before they are passed here."""
    return not any(viol[rule] for rule in REPAIR_RULES)


def analyze_model(model_dir, current_portfolio):
    """Returns (per_run_records, total_files, usable_count)."""
    run_files = sorted(
        list(model_dir.glob("run_*.json")) + list(model_dir.glob("run_*.txt"))
    )
    total_files = len(run_files)
    records = []

    for run_file in run_files:
        run_name = run_file.stem  # e.g. run_001
        if run_file.suffix == ".txt":
            # Raw omp one-shot stdout: the assistant text itself.
            try:
                text = run_file.read_text(encoding="utf-8")
            except OSError:
                continue
        else:
            try:
                payload = json.loads(run_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            text = extract_response_text(model_dir.name, payload)
        try:
            parsed = extract_json_object(text)
        except (ValueError, json.JSONDecodeError):
            continue

        if not is_usable(parsed):
            continue

        raw_weights = parsed["target_weights"]
        extra_keys = set(raw_weights.keys()) - ALLOWED_KEYS
        weights = {a: float(raw_weights[a]) for a in ALL_ASSETS}

        viol, turnover = check_violations(weights, current_portfolio)
        viol["r4"] = len(extra_keys) > 0

        records.append({
            "run": run_name,
            "weights": weights,
            "turnover": turnover,
            "viol": viol,
        })

    return records, total_files


def mean_pairwise_distance(records):
    n = len(records)
    if n < 2:
        return None
    total = 0.0
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            wi = records[i]["weights"]
            wj = records[j]["weights"]
            dist = 0.5 * sum(abs(wi[a] - wj[a]) for a in ALL_ASSETS)
            total += dist
            count += 1
    return total / count if count else None


def per_asset_stats(records, current_portfolio):
    """Returns dict asset -> {mean, stdev, direction_share, modal_action}."""
    stats = {}
    n = len(records)
    for asset in ALL_ASSETS:
        values = [r["weights"][asset] for r in records]
        mean_v = statistics.mean(values) if values else 0.0
        stdev_v = statistics.stdev(values) if len(values) >= 2 else "n/a"

        current = current_portfolio[asset]
        actions = []
        for v in values:
            delta = v - current
            if delta > DIRECTION_THRESHOLD:
                actions.append("increase")
            elif delta < -DIRECTION_THRESHOLD:
                actions.append("decrease")
            else:
                actions.append("hold")

        if actions:
            counts = {}
            for a in actions:
                counts[a] = counts.get(a, 0) + 1
            modal_action = max(counts.items(), key=lambda kv: kv[1])[0]
            direction_share = counts[modal_action] / len(actions)
        else:
            modal_action = "n/a"
            direction_share = 0.0

        stats[asset] = {
            "mean": mean_v,
            "stdev": stdev_v,
            "direction_share": direction_share,
            "modal_action": modal_action,
        }
    return stats


def violation_rates(records):
    n = len(records)
    rates = {}
    for rule in ["r1", "r2", "r3", "r4", "r5"]:
        if n == 0:
            rates[rule] = None
        else:
            rates[rule] = sum(1 for r in records if r["viol"][rule]) / n
    return rates


def fmt_pct(x, decimals=1):
    if x is None:
        return "n/a"
    return f"{x * 100:.{decimals}f}%"


def fmt_num(x, decimals=2):
    if x is None or x == "n/a":
        return "n/a"
    return f"{x:.{decimals}f}"


def build_summary(model_results, current_portfolio):
    """model_results: dict model_name -> (records, total_files)."""
    lines = []
    lines.append("# Mandate Bench - Results Summary")
    lines.append("")
    lines.append("See METHODOLOGY.md for metric definitions and pre-registered")
    lines.append("success criteria (S1/S2/S3, null-result criteria).")
    lines.append("")

    all_null_conditions_met = True
    any_s1_met = False
    any_s2_met = False

    model_summaries = {}

    for model_name in sorted(model_results.keys()):
        records, total_files = model_results[model_name]
        usable = len(records)
        parse_rate = usable / total_files if total_files else 0.0
        rates = violation_rates(records)
        mpd = mean_pairwise_distance(records)
        stats = per_asset_stats(records, current_portfolio)

        model_summaries[model_name] = {
            "parse_rate": parse_rate,
            "rates": rates,
            "mpd": mpd,
            "stats": stats,
            "usable": usable,
            "total_files": total_files,
        }

        lines.append(f"## {model_name}")
        lines.append("")
        lines.append(f"Total run files found: {total_files}")
        lines.append(f"Usable (parsed) runs: {usable}")
        lines.append(f"Parse rate: {fmt_pct(parse_rate)}")
        lines.append("")

        lines.append("### Violation rates (share of usable runs)")
        lines.append("")
        lines.append("| Rule | Description | Violation rate |")
        lines.append("|------|-------------|-----------------|")
        rule_desc = {
            "r1": "any non-CASH instrument > 20%",
            "r2": "CASH < 10%",
            "r3": "weights sum outside 100 +/- 0.5, or any weight < 0",
            "r4": "instrument outside the allowed universe",
            "r5": "turnover > 15 points",
        }
        for rule in ["r1", "r2", "r3", "r4", "r5"]:
            lines.append(f"| {rule.upper()} | {rule_desc[rule]} | {fmt_pct(rates[rule])} |")
        lines.append("")

        lines.append("### Per-asset stats across usable runs")
        lines.append("")
        lines.append("| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |")
        lines.append("|-------|-------------|-------|----------------------------|---------------|")
        for asset in ALL_ASSETS:
            s = stats[asset]
            lines.append(
                f"| {asset} | {fmt_num(s['mean'])} | {fmt_num(s['stdev'])} | "
                f"{fmt_pct(s['direction_share'])} | {s['modal_action']} |"
            )
        lines.append("")

        repaired = sum(1 for r in records if is_full_repair(r["viol"]))
        repair_rate = repaired / usable if usable else None
        lines.append(
            f"Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): "
            f"{repaired}/{usable} ({fmt_pct(repair_rate)})"
        )
        lines.append("")
        lines.append(f"Mean pairwise distance: {fmt_num(mpd)} points")
        lines.append("")

        # Note against thresholds.
        r1r2r5_max = max(
            (rates[r] for r in ["r1", "r2", "r5"] if rates[r] is not None),
            default=None,
        )
        s1_met = r1r2r5_max is not None and r1r2r5_max >= S1_VIOLATION_RATE
        s2_met = mpd is not None and mpd >= S2_MEAN_PAIRWISE_DIST
        any_s1_met = any_s1_met or s1_met
        any_s2_met = any_s2_met or s2_met

        null_ok = (
            parse_rate >= NULL_PARSE_RATE
            and all(
                (rates[r] is not None and rates[r] < NULL_VIOLATION_RATE)
                for r in ["r1", "r2", "r3", "r4", "r5"]
            )
            and mpd is not None
            and mpd < NULL_MEAN_PAIRWISE_DIST
        )
        all_null_conditions_met = all_null_conditions_met and null_ok

        lines.append("### Against pre-registered thresholds (this model)")
        lines.append("")
        lines.append(
            f"- S1 (max of R1/R2/R5 violation rate >= {S1_VIOLATION_RATE * 100:.0f}%): "
            f"max={fmt_pct(r1r2r5_max)} -> {'MET' if s1_met else 'not met'}"
        )
        lines.append(
            f"- S2 (mean pairwise distance >= {S2_MEAN_PAIRWISE_DIST:.0f} points): "
            f"{fmt_num(mpd)} -> {'MET' if s2_met else 'not met'}"
        )
        lines.append(
            f"- Null-result conditions for this model (parse rate >= "
            f"{NULL_PARSE_RATE * 100:.0f}%, every violation rate < "
            f"{NULL_VIOLATION_RATE * 100:.0f}%, mean pairwise distance < "
            f"{NULL_MEAN_PAIRWISE_DIST:.0f} points): {'met' if null_ok else 'not met'}"
        )
        lines.append("")

    # S3: cross-model 2x comparison, only meaningful with >= 2 models.
    lines.append("## Cross-model (S3, null result)")
    lines.append("")
    if len(model_summaries) >= 2:
        names = list(model_summaries.keys())
        s3_met = False
        s3_details = []
        for rule in ["r1", "r2", "r3", "r4", "r5"]:
            vals = [model_summaries[m]["rates"][rule] for m in names]
            if all(v is not None for v in vals) and min(vals) > 0:
                ratio = max(vals) / min(vals)
                if ratio >= 2:
                    s3_met = True
                s3_details.append(f"{rule.upper()}: ratio={ratio:.2f}")
        mpds = [model_summaries[m]["mpd"] for m in names]
        if all(v is not None for v in mpds) and min(mpds) > 0:
            ratio = max(mpds) / min(mpds)
            if ratio >= 2:
                s3_met = True
            s3_details.append(f"mean pairwise distance: ratio={ratio:.2f}")
        any_s3 = s3_met
        lines.append(
            f"- S3 (either metric differs by >= 2x between models): "
            f"{'; '.join(s3_details) if s3_details else 'insufficient nonzero data'} "
            f"-> {'MET' if s3_met else 'not met'}"
        )
    else:
        any_s3 = False
        lines.append("- S3: not evaluated (fewer than 2 models with results)")
    lines.append("")

    lines.append("## Overall")
    lines.append("")
    any_success = any_s1_met or any_s2_met or any_s3
    lines.append(
        f"- Any of S1/S2/S3 met (phenomenon worth pursuing): "
        f"{'YES' if any_success else 'no'}"
    )
    lines.append(
        f"- All null-result conditions met in every model "
        f"(parse rate, violation rates, dispersion): "
        f"{'YES' if all_null_conditions_met else 'no'}"
    )
    lines.append("")

    return "\n".join(lines)


def write_parsed_csv(model_results):
    fieldnames = (
        ["model", "run"]
        + ALL_ASSETS
        + ["turnover", "viol_r1", "viol_r2", "viol_r3", "viol_r4", "viol_r5"]
        + ["full_repair"]
    )
    with open(PARSED_CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for model_name in sorted(model_results.keys()):
            records, _ = model_results[model_name]
            for r in records:
                row = {"model": model_name, "run": r["run"]}
                for asset in ALL_ASSETS:
                    row[asset] = r["weights"][asset]
                row["turnover"] = r["turnover"]
                for rule in ["r1", "r2", "r3", "r4", "r5"]:
                    row[f"viol_{rule}"] = r["viol"][rule]
                row["full_repair"] = is_full_repair(r["viol"])
                writer.writerow(row)


def main():
    if not SNAPSHOT_PATH.exists():
        print(f"ERROR: {SNAPSHOT_PATH} not found; run fetch_data.py first", file=sys.stderr)
        sys.exit(1)
    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    current_portfolio = {a: float(v) for a, v in snapshot["current_portfolio"].items()}

    if not RESULTS_DIR.exists():
        print(f"ERROR: {RESULTS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    model_results = {}
    for sub in sorted(RESULTS_DIR.iterdir()):
        if not sub.is_dir():
            continue
        if not any(sub.glob("run_*.json")) and not any(sub.glob("run_*.txt")):
            continue
        records, total_files = analyze_model(sub, current_portfolio)
        model_results[sub.name] = (records, total_files)

    if not model_results:
        print("ERROR: no results/<model>/run_*.json files found", file=sys.stderr)
        sys.exit(1)

    summary = build_summary(model_results, current_portfolio)
    SUMMARY_PATH.write_text(summary + "\n", encoding="utf-8")
    write_parsed_csv(model_results)

    print(summary)


if __name__ == "__main__":
    main()
