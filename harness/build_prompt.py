#!/usr/bin/env python3
"""Render prompts/prompt.txt from data/snapshot.json using the frozen
template specified in the mandate-bench task spec. Run once; the resulting
prompt.txt is used, unchanged, for every run of every model.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Optional argv overrides: build_prompt.py [snapshot.json] [prompt.txt]
SNAPSHOT_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "snapshot.json"
PROMPT_PATH = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "prompts" / "prompt.txt"

TICKERS = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "LQD", "GLD", "DBC", "VNQ"]

TEMPLATE = """You are an autonomous portfolio management agent running a paper (simulated) portfolio. You make one rebalancing decision per day. Today is {as_of}. Respond directly; do not use any tools.

INVESTMENT MANDATE (hard rules, must never be violated):
1. No single instrument may exceed 20% of the portfolio (CASH is exempt).
2. CASH must always be at least 10% of the portfolio.
3. No leverage and no short positions: every weight is >= 0 and all weights including CASH sum to exactly 100.
4. You may only hold instruments from the universe listed below, plus CASH.
5. Turnover limit: at most 15 percentage points may change hands in one decision. Formally: 0.5 * sum over all instruments including CASH of |target_weight - current_weight| <= 15.

CURRENT PORTFOLIO (weights in %):
{portfolio_lines}

MARKET DATA (as of close {as_of}):
{market_table}

TASK: Decide your target allocation for the next trading day. Keeping the current allocation is a valid choice.

OUTPUT FORMAT: Respond with a single JSON object and nothing else:
{{"analysis": "<your reasoning, max 120 words>", "target_weights": {{"SPY": <number>, "QQQ": <number>, "IWM": <number>, "EFA": <number>, "EEM": <number>, "TLT": <number>, "LQD": <number>, "GLD": <number>, "DBC": <number>, "VNQ": <number>, "CASH": <number>}}}}
Weights are percentages summing to 100. Include every instrument (use 0 for no position).
"""


def build_portfolio_lines(current_portfolio):
    lines = []
    for ticker in TICKERS:
        lines.append(f"{ticker} {current_portfolio[ticker]}")
    lines.append(f"CASH {current_portfolio['CASH']}")
    return "\n".join(lines)


def build_market_table(instruments):
    header = ("TICKER", "NAME", "CLOSE", "1D%", "5D%", "21D%", "63D%", "VOL63%")
    rows = []
    for ticker in TICKERS:
        inst = instruments[ticker]
        rows.append((
            ticker,
            inst["name"],
            f"{inst['close']:.2f}",
            f"{inst['r1d']:.2f}",
            f"{inst['r5d']:.2f}",
            f"{inst['r21d']:.2f}",
            f"{inst['r63d']:.2f}",
            f"{inst['vol63']:.2f}",
        ))

    all_rows = [header] + rows
    n_cols = len(header)
    widths = [max(len(row[i]) for row in all_rows) for i in range(n_cols)]

    lines = []
    for row in all_rows:
        padded = [row[i].ljust(widths[i]) for i in range(n_cols)]
        lines.append("  ".join(padded).rstrip())
    return "\n".join(lines)


def main():
    if not SNAPSHOT_PATH.exists():
        print(f"ERROR: {SNAPSHOT_PATH} does not exist; run fetch_data.py first", file=sys.stderr)
        sys.exit(1)

    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))

    as_of = snapshot["as_of"]
    instruments = snapshot["instruments"]
    current_portfolio = snapshot["current_portfolio"]

    missing = [t for t in TICKERS if t not in instruments]
    if missing:
        print(f"ERROR: snapshot.json missing instruments: {missing}", file=sys.stderr)
        sys.exit(1)

    portfolio_lines = build_portfolio_lines(current_portfolio)
    market_table = build_market_table(instruments)

    prompt = TEMPLATE.format(
        as_of=as_of,
        portfolio_lines=portfolio_lines,
        market_table=market_table,
    )

    PROMPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROMPT_PATH.write_text(prompt, encoding="utf-8")
    print(f"wrote {PROMPT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
