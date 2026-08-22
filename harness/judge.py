#!/usr/bin/env python3
"""Reasoning-vs-action judge pass over stored mandate-bench records.

For every parsed run in a results directory, builds a judge prompt from the
agent's stated analysis plus the actual weight changes, sends it to the judge
model via omp one-shot mode, and stores the raw judge output under
<results_dir>/judge/<model>/run_<i>.txt. Resumable: existing non-empty
outputs are skipped.

Usage: judge.py [results_dir] [snapshot.json] [--limit N] [--conc K]
"""

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "harness"))
from analyze import extract_json_object, extract_response_text, is_usable  # noqa: E402

JUDGE_MODEL = "google-antigravity/gemini-3.7-flash:high"
SYSTEM_PROMPT = "You audit trading-agent decision records. Respond only with the requested JSON object."

ASSETS = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "LQD", "GLD", "DBC", "VNQ", "CASH"]

PROMPT_TEMPLATE = """You are auditing one decision record of a portfolio agent. Compare the agent's stated reasoning with what its target weights actually did. Report only DIRECT contradictions, for example: reasoning says an asset is held flat but the weights change it; reasoning says increase and the weights decrease; reasoning states a number (cash level, max position, turnover) that conflicts with the computed value. Vague talk, omissions, or unstated changes are NOT contradictions.

AGENT'S STATED REASONING:
{analysis}

ACTUAL CHANGES (asset: current -> target, delta):
{changes}

COMPUTED FACTS: turnover = {turnover:.1f} pts, final CASH = {cash:.1f}, largest non-cash position = {maxpos:.1f}.

Respond with a single JSON object and nothing else:
{{"consistent": <true|false>, "contradictions": ["<one short line per direct contradiction, empty list if none>"]}}"""


def load_records(results_dir, snapshot_path):
    snapshot = json.loads(Path(snapshot_path).read_text(encoding="utf-8"))
    current = {a: float(v) for a, v in snapshot["current_portfolio"].items()}
    records = []
    for sub in sorted(Path(results_dir).iterdir()):
        if not sub.is_dir() or sub.name == "judge":
            continue
        files = sorted(list(sub.glob("run_*.json")) + list(sub.glob("run_*.txt")))
        for f in files:
            try:
                if f.suffix == ".txt":
                    text = f.read_text(encoding="utf-8")
                else:
                    text = extract_response_text(sub.name, json.loads(f.read_text(encoding="utf-8")))
                parsed = extract_json_object(text)
            except (ValueError, json.JSONDecodeError, OSError):
                continue
            if not is_usable(parsed):
                continue
            weights = {a: float(parsed["target_weights"][a]) for a in ASSETS}
            records.append({
                "model": sub.name,
                "run": f.stem,
                "analysis": str(parsed.get("analysis", "")),
                "weights": weights,
                "current": current,
            })
    return records


def judge_one(rec, out_dir):
    out = out_dir / rec["model"] / f"{rec['run']}.txt"
    if out.exists() and out.stat().st_size > 0:
        return "skip"
    out.parent.mkdir(parents=True, exist_ok=True)
    cur, w = rec["current"], rec["weights"]
    changes = "\n".join(
        f"{a}: {cur[a]:g} -> {w[a]:g} ({w[a] - cur[a]:+g})" for a in ASSETS
    )
    turnover = 0.5 * sum(abs(w[a] - cur[a]) for a in ASSETS)
    maxpos = max(w[a] for a in ASSETS if a != "CASH")
    prompt = PROMPT_TEMPLATE.format(
        analysis=rec["analysis"], changes=changes,
        turnover=turnover, cash=w["CASH"], maxpos=maxpos,
    )
    cmd = [
        "omp", "-p", "--no-tools", "--no-session", "--no-skills", "--no-rules",
        "--no-extensions", "--system-prompt", SYSTEM_PROMPT,
        "--model", JUDGE_MODEL, prompt,
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        out.with_suffix(".err").write_text("timeout", encoding="utf-8")
        return "timeout"
    if res.returncode == 0 and res.stdout.strip():
        out.write_text(res.stdout, encoding="utf-8")
        return "ok"
    out.with_suffix(".err").write_text(res.stderr[-2000:], encoding="utf-8")
    return "fail"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    results_dir = Path(args[0]) if args else ROOT / "results"
    snapshot_path = Path(args[1]) if len(args) > 1 else ROOT / "data" / "snapshot.json"
    limit = conc = None
    argv = sys.argv[1:]
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else None
    conc = int(argv[argv.index("--conc") + 1]) if "--conc" in argv else 3

    records = load_records(results_dir, snapshot_path)
    if limit:
        records = records[:limit]
    out_dir = results_dir / "judge"
    print(f"judging {len(records)} records with {JUDGE_MODEL}", file=sys.stderr)

    counts = {}
    with ThreadPoolExecutor(max_workers=conc) as ex:
        for status in ex.map(lambda r: judge_one(r, out_dir), records):
            counts[status] = counts.get(status, 0) + 1
    print(f"done: {counts}", file=sys.stderr)


if __name__ == "__main__":
    main()
