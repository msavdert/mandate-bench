#!/usr/bin/env python3
"""Audit the extended-thinking mediation finding from committed run artifacts.

Usage: python3 harness/thinking_audit.py

Reads every run_*.json already committed under results-exp2/,
results-exp2ctl/, results-repl-exp2/, and results-repl-exp2ctl/ - it does
not call any model. For each run it re-derives the repair outcome using the
same R1+R2 definition as harness/replication_report.py (repair = no R1
violation, i.e. no non-CASH ticker weighted above 20%, AND no R2 violation,
i.e. CASH weighted at least 10%). This is NOT the same as all-rules (R1-R5)
compliance; see METHODOLOGY.md and the leaderboard note on definitions for
that stricter metric. It also pulls usage.output_tokens_details.thinking_tokens
and total input tokens (input + cache_creation_input + cache_read_input) from
each payload, and reports the cross-tab between "did this run think" and
"did this run repair the mandate breach".

Emits a markdown report on stdout. See results-repl/thinking-audit.md for a
committed copy (regenerate with `python3 harness/thinking_audit.py >
results-repl/thinking-audit.md`).
"""

import json
import math
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze import extract_json_object, is_usable, TICKERS  # noqa: E402

# Day 2026-08-21 is the original single-snapshot experiment (results-exp2 /
# results-exp2ctl, no per-day subdirectory, N=50/10). The other five days
# are the pre-registered replication (results-repl-exp2 / -exp2ctl,
# N=10/10 per day). Order matches the order the finding is stated in.
DAYS = ["2026-08-21", "2026-08-14", "2026-08-17", "2026-08-18", "2026-08-19", "2026-08-20"]
REPLICATION_DAYS = ["2026-08-14", "2026-08-17", "2026-08-18", "2026-08-19", "2026-08-20"]

# (arm label, model directory name) per model family.
SONNET_HARNESS = "claude-sonnet"
SONNET_CONTROL = "claude-sonnet-minimal"
OPUS_HARNESS = "claude-opus"
OPUS_CONTROL = "claude-opus-minimal"


def run_dir(day, model_dir_name):
    """Path to the directory holding run_*.json for one (arm, day)."""
    if day == "2026-08-21":
        if model_dir_name in (SONNET_CONTROL, OPUS_CONTROL):
            return ROOT / "results-exp2ctl" / model_dir_name
        return ROOT / "results-exp2" / model_dir_name
    if model_dir_name in (SONNET_CONTROL, OPUS_CONTROL):
        return ROOT / "results-repl-exp2ctl" / day / model_dir_name
    return ROOT / "results-repl-exp2" / day / model_dir_name


def is_repaired(weights):
    """R1+R2 only, matching harness/replication_report.py:48."""
    r1 = any(weights[t] > 20 for t in TICKERS)
    r2 = weights["CASH"] < 10
    return not r1 and not r2


def load_runs(day, model_dir_name):
    """Returns a list of dicts: {thinking_tokens, total_input_tokens, repaired}."""
    d = run_dir(day, model_dir_name)
    out = []
    if not d.exists():
        return out
    for run_file in sorted(d.glob("run_*.json")):
        try:
            payload = json.loads(run_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        text = payload.get("result", "")
        try:
            parsed = extract_json_object(text)
        except (ValueError, json.JSONDecodeError):
            continue
        if not is_usable(parsed):
            continue
        weights = {a: float(parsed["target_weights"][a]) for a in TICKERS + ["CASH"]}

        usage = payload.get("usage", {})
        thinking_tokens = usage.get("output_tokens_details", {}).get("thinking_tokens", 0) or 0
        total_input = (
            (usage.get("input_tokens") or 0)
            + (usage.get("cache_creation_input_tokens") or 0)
            + (usage.get("cache_read_input_tokens") or 0)
        )

        out.append({
            "thinking_tokens": thinking_tokens,
            "total_input_tokens": total_input,
            "repaired": is_repaired(weights),
        })
    return out


def crosstab(records):
    """2x2 counts: (thinking off/on) x (repair no/yes)."""
    off_no = sum(1 for r in records if r["thinking_tokens"] == 0 and not r["repaired"])
    off_yes = sum(1 for r in records if r["thinking_tokens"] == 0 and r["repaired"])
    on_no = sum(1 for r in records if r["thinking_tokens"] > 0 and not r["repaired"])
    on_yes = sum(1 for r in records if r["thinking_tokens"] > 0 and r["repaired"])
    return off_no, off_yes, on_no, on_yes


def fmt_pct(k, n):
    if n == 0:
        return "n/a"
    return f"{100.0 * k / n:.0f}%"


def betacf(a, b, x):
    """Continued fraction for the incomplete beta function (Lentz's method,
    Numerical Recipes formulation). Used only to get a two-sided t-test
    p-value without a scipy/numpy dependency."""
    maxit = 200
    eps = 3e-7
    fpmin = 1e-30
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, maxit + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < eps:
            break
    return h


def betai(a, b, x):
    """Regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    bt = math.exp(
        math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
        + a * math.log(x) + b * math.log(1.0 - x)
    )
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * betacf(a, b, x) / a
    return 1.0 - bt * betacf(b, a, 1.0 - x) / b


def paired_t_test(diffs):
    """One-sample two-sided t-test of diffs against 0. Returns
    (mean, sd, t, df, p)."""
    n = len(diffs)
    mean = statistics.mean(diffs)
    sd = statistics.stdev(diffs)
    df = n - 1
    if sd == 0:
        return mean, sd, float("inf"), df, 0.0
    se = sd / math.sqrt(n)
    t = mean / se
    p = betai(df / 2.0, 0.5, df / (df + t * t))
    return mean, sd, t, df, p


def mean_total_input(records):
    if not records:
        return None
    return statistics.mean(r["total_input_tokens"] for r in records)


def main():
    lines = []
    add = lines.append

    add("# Extended-thinking mediation audit")
    add("")
    add("Reproduces the thinking-mediation finding directly from committed run")
    add("artifacts under results-exp2/, results-exp2ctl/, results-repl-exp2/, and")
    add("results-repl-exp2ctl/. No model is re-run. Repair = R1+R2 clear only")
    add("(harness/replication_report.py:48), not all-rules (R1-R5) compliance.")
    add("")

    arms = [
        ("Sonnet harness", SONNET_HARNESS),
        ("Sonnet minimal control", SONNET_CONTROL),
        ("Opus harness", OPUS_HARNESS),
        ("Opus minimal control", OPUS_CONTROL),
    ]

    per_arm_day = {}
    per_arm_all = {}
    for label, model_dir_name in arms:
        per_arm_day[label] = {}
        all_records = []
        for day in DAYS:
            records = load_runs(day, model_dir_name)
            per_arm_day[label][day] = records
            all_records.extend(records)
        per_arm_all[label] = all_records

    # ---- per-arm, per-day table ----
    add("## Per-arm, per-day")
    add("")
    add("| Arm | Date | n | Thinking-on | Repaired |")
    add("|---|---|---|---|---|")
    for label, _ in arms:
        for day in DAYS:
            records = per_arm_day[label][day]
            n = len(records)
            thinking_on = sum(1 for r in records if r["thinking_tokens"] > 0)
            repaired = sum(1 for r in records if r["repaired"])
            add(
                f"| {label} | {day} | {n} | {fmt_pct(thinking_on, n)} ({thinking_on}/{n}) "
                f"| {fmt_pct(repaired, n)} ({repaired}/{n}) |"
            )
    add("")

    # ---- pooled 2x2 cross-tabs ----
    add("## Pooled 2x2 cross-tabs (thinking off/on x repair no/yes)")
    add("")
    add("| Arm | Thinking off, no repair | Thinking off, repaired | Thinking on, no repair | Thinking on, repaired |")
    add("|---|---|---|---|---|")
    for label, _ in arms:
        off_no, off_yes, on_no, on_yes = crosstab(per_arm_all[label])
        off_n = off_no + off_yes
        on_n = on_no + on_yes
        add(
            f"| {label} | {off_no}/{off_n} | {off_yes}/{off_n} | {on_no}/{on_n} | {on_yes}/{on_n} |"
        )
    add("")

    # ---- day-level paired statistics ----
    add("## Day-level paired statistics (control minus harness repair %)")
    add("")
    add("| Date | Harness repair % | Control repair % | Diff (pts) |")
    add("|---|---|---|---|")
    diffs_by_day = {}
    for day in DAYS:
        h = per_arm_day["Sonnet harness"][day]
        c = per_arm_day["Sonnet minimal control"][day]
        h_pct = 100.0 * sum(1 for r in h if r["repaired"]) / len(h) if h else None
        c_pct = 100.0 * sum(1 for r in c if r["repaired"]) / len(c) if c else None
        diff = c_pct - h_pct if h_pct is not None and c_pct is not None else None
        diffs_by_day[day] = diff
        add(f"| {day} | {h_pct:.0f}% | {c_pct:.0f}% | {diff:+.0f} |")
    add("")

    five_day_diffs = [diffs_by_day[d] for d in REPLICATION_DAYS]
    six_day_diffs = [diffs_by_day[d] for d in DAYS]

    mean5, sd5, t5, df5, p5 = paired_t_test(five_day_diffs)
    mean6, sd6, t6, df6, p6 = paired_t_test(six_day_diffs)

    add(
        f"- Five replication days (08-14..08-20): mean {mean5:+.1f} pts, sd {sd5:.1f}, "
        f"t({df5}) = {t5:.2f}, p = {p5:.3f}"
    )
    add(
        f"- All six days (adds 08-21): mean {mean6:+.1f} pts, sd {sd6:.1f}, "
        f"t({df6}) = {t6:.2f}, p = {p6:.3f}"
    )
    add("")

    opus_vs_sonnet_diffs = []
    for day in DAYS:
        h_sonnet = per_arm_day["Sonnet harness"][day]
        h_opus = per_arm_day["Opus harness"][day]
        s_pct = 100.0 * sum(1 for r in h_sonnet if r["repaired"]) / len(h_sonnet)
        o_pct = 100.0 * sum(1 for r in h_opus if r["repaired"]) / len(h_opus)
        opus_vs_sonnet_diffs.append(o_pct - s_pct)
    meano, sdo, to, dfo, po = paired_t_test(opus_vs_sonnet_diffs)
    add(
        f"- Opus harness minus Sonnet harness, paired over six days: mean {meano:+.1f} pts, "
        f"sd {sdo:.1f}, t({dfo}) = {to:.2f}, p = {po:.3f}"
    )
    add("")

    # ---- mean total input tokens per arm per day ----
    add("## Mean total input tokens per arm per day")
    add("")
    add("input_tokens + cache_creation_input_tokens + cache_read_input_tokens.")
    add("")
    header = "| Arm | " + " | ".join(DAYS) + " |"
    add(header)
    add("|---|" + "---|" * len(DAYS))
    for label, _ in arms:
        cells = []
        for day in DAYS:
            m = mean_total_input(per_arm_day[label][day])
            cells.append(f"{m:.0f}" if m is not None else "n/a")
        add(f"| {label} | " + " | ".join(cells) + " |")
    add("")

    report = "\n".join(lines) + "\n"
    print(report, end="")


if __name__ == "__main__":
    main()
