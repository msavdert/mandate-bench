#!/usr/bin/env python3
"""Summarize judge outputs: contradiction rate per model.

Usage: judge_analyze.py [results_dir]
Writes <results_dir>/judge/summary.md and prints it.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "harness"))
from analyze import extract_json_object  # noqa: E402


def main():
    results_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "results"
    judge_dir = results_dir / "judge"
    if not judge_dir.exists():
        print(f"ERROR: {judge_dir} not found", file=sys.stderr)
        sys.exit(1)

    lines = ["# Judge pass summary", ""]
    lines.append("| Model | Judged | Parsed | Inconsistent | Rate | Example contradiction |")
    lines.append("|---|---|---|---|---|---|")
    details = []
    for sub in sorted(judge_dir.iterdir()):
        if not sub.is_dir():
            continue
        total = parsed_n = incons = 0
        example = ""
        for f in sorted(sub.glob("run_*.txt")):
            total += 1
            try:
                verdict = extract_json_object(f.read_text(encoding="utf-8"))
            except (ValueError, json.JSONDecodeError, OSError):
                continue
            if not isinstance(verdict, dict) or "consistent" not in verdict:
                continue
            parsed_n += 1
            if not verdict.get("consistent", True):
                incons += 1
                cons = verdict.get("contradictions") or []
                if cons:
                    details.append(f"- {sub.name}/{f.stem}: {cons[0]}")
                    if not example:
                        example = str(cons[0])[:80]
        rate = f"{100.0 * incons / parsed_n:.1f}%" if parsed_n else "n/a"
        lines.append(f"| {sub.name} | {total} | {parsed_n} | {incons} | {rate} | {example} |")

    lines.append("")
    lines.append("## All flagged contradictions")
    lines.extend(details if details else ["- none"])
    out = "\n".join(lines)
    (judge_dir / "summary.md").write_text(out + "\n", encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
