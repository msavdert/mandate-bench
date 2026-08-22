#!/usr/bin/env python3
"""Build a snapshot for a historical as-of date from the committed Yahoo
chart JSON in data/, without any network access.

Usage: make_snapshot.py <as_of YYYY-MM-DD> <out.json> [portfolio.json]

Reuses parse_rows/compute_stats from fetch_data.py unchanged, truncating
each ticker's history at the as-of date. The optional third argument is a
JSON file whose "current_portfolio" replaces the default compliant
portfolio (used for the Experiment 2 violating start). Pre-registered in
METHODOLOGY.md Amendment 3. Fails loudly if any ticker lacks a row for the
requested date or has fewer than MIN_ROWS rows up to it.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_data import (  # noqa: E402
    CURRENT_PORTFOLIO, DATA_DIR, MIN_ROWS, NAMES, TICKERS,
    compute_stats, parse_rows,
)


def main():
    if len(sys.argv) not in (3, 4):
        sys.exit("usage: make_snapshot.py <as_of YYYY-MM-DD> <out.json> [portfolio.json]")
    as_of, out_path = sys.argv[1], Path(sys.argv[2])
    portfolio = CURRENT_PORTFOLIO
    if len(sys.argv) == 4:
        portfolio = json.loads(Path(sys.argv[3]).read_text())["current_portfolio"]

    instruments = {}
    for ticker in TICKERS:
        raw = (DATA_DIR / f"{ticker}.yahoo.json").read_text(encoding="utf-8")
        rows = [r for r in parse_rows(ticker, raw) if r[0] <= as_of]
        if not rows or rows[-1][0] != as_of:
            raise RuntimeError(f"{ticker}: no row for as_of date {as_of}")
        if len(rows) < MIN_ROWS:
            raise RuntimeError(
                f"{ticker}: only {len(rows)} rows up to {as_of}, need {MIN_ROWS}"
            )
        stats = compute_stats([c for _, c in rows])
        instruments[ticker] = {
            "name": NAMES[ticker],
            "close": round(stats["close"], 2),
            "r1d": round(stats["r1d"], 2),
            "r5d": round(stats["r5d"], 2),
            "r21d": round(stats["r21d"], 2),
            "r63d": round(stats["r63d"], 2),
            "vol63": round(stats["vol63"], 2),
        }

    snapshot = {
        "as_of": as_of,
        "instruments": instruments,
        "current_portfolio": portfolio,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_path} (as_of={as_of})", file=sys.stderr)


if __name__ == "__main__":
    main()
