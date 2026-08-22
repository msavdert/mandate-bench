#!/usr/bin/env python3
"""Fetch daily OHLC history from Stooq for the mandate-bench universe and
compute the market snapshot used to render the frozen prompt.

Writes:
  data/<TICKER>.us.csv  - raw Stooq CSV response, one per ticker
  data/snapshot.json    - computed stats, see METHODOLOGY.md / build_prompt.py

Fails loudly (nonzero exit, clear message) on any network error, HTTP error,
or data that looks wrong (HTML instead of CSV, too few rows). Never
fabricates or silently substitutes data.
"""

import datetime
import json
import math
import statistics
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

TICKERS = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "LQD", "GLD", "DBC", "VNQ"]

NAMES = {
    "SPY": "S&P 500 ETF",
    "QQQ": "Nasdaq-100 ETF",
    "IWM": "Russell 2000 ETF",
    "EFA": "MSCI EAFE ETF",
    "EEM": "MSCI Emerging Markets ETF",
    "TLT": "20+ Year Treasury ETF",
    "LQD": "Investment Grade Corporate Bond ETF",
    "GLD": "Gold ETF",
    "DBC": "Commodity Index ETF",
    "VNQ": "US Real Estate ETF",
}

CURRENT_PORTFOLIO = {
    "SPY": 18, "QQQ": 15, "IWM": 5, "EFA": 8, "EEM": 4,
    "TLT": 12, "LQD": 8, "GLD": 10, "DBC": 3, "VNQ": 5, "CASH": 12,
}

# Stooq blocks this VM's egress IP with a JS anti-bot challenge (verified
# 2026-08-21), so daily closes come from the Yahoo Finance chart endpoint
# instead. Unofficial API, research snapshot use only.
YAHOO_URL = (
    "https://query1.finance.yahoo.com/v8/finance/chart/"
    "{ticker}?range=1y&interval=1d"
)
# Yahoo's edge 429s the full Chrome UA string from this IP but accepts the
# bare token (verified 2026-08-21). Do not "fix" this back to a full UA.
USER_AGENT = "Mozilla/5.0"

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

MIN_ROWS = 64  # need at least 63 trading days of returns plus one anchor close


def fetch_csv(ticker):
    """Download raw chart JSON for one ticker from Yahoo. Raises on failure."""
    url = YAHOO_URL.format(ticker=ticker.upper())
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_err = None
    for attempt in range(4):
        if attempt:
            time.sleep(5 * attempt)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                status = resp.status
                body = resp.read().decode("utf-8", errors="replace")
            break
        except urllib.error.HTTPError as e:
            last_err = RuntimeError(f"{ticker}: HTTP error {e.code} fetching {url}")
            if e.code not in (429, 500, 502, 503):
                raise last_err from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"{ticker}: network error fetching {url}: {e.reason}") from e
    else:
        raise last_err

    if status != 200:
        raise RuntimeError(f"{ticker}: unexpected HTTP status {status} from {url}")
    if not body.strip():
        raise RuntimeError(f"{ticker}: empty response from {url}")
    return body


def parse_rows(ticker, raw_json):
    """Parse Yahoo chart JSON into a list of (date_str, close) sorted oldest-first."""
    try:
        payload = json.loads(raw_json)
        result = payload["chart"]["result"][0]
        timestamps = result["timestamp"]
        closes = result["indicators"]["quote"][0]["close"]
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
        raise RuntimeError(f"{ticker}: unexpected Yahoo response shape: {e}") from e

    if len(timestamps) != len(closes):
        raise RuntimeError(
            f"{ticker}: timestamp/close length mismatch "
            f"({len(timestamps)} vs {len(closes)})"
        )

    rows = []
    for ts, close in zip(timestamps, closes):
        if close is None:
            continue
        date = datetime.date.fromtimestamp(ts).isoformat()
        rows.append((date, float(close)))

    if len(rows) < MIN_ROWS:
        raise RuntimeError(
            f"{ticker}: only {len(rows)} usable rows parsed, need at least {MIN_ROWS} "
            f"for 63-day stats"
        )

    rows.sort(key=lambda r: r[0])
    # Yahoo can emit duplicate dates (e.g. a live intraday row plus the daily
    # row); keep the last occurrence of each date.
    deduped = {}
    for date, close in rows:
        deduped[date] = close
    return sorted(deduped.items())


def compute_stats(closes):
    """closes: list of floats, oldest-first, at least MIN_ROWS long.
    Returns dict with close, r1d, r5d, r21d, r63d, vol63 (unrounded)."""
    last = closes[-1]

    def pct_return(n):
        prior = closes[-1 - n]
        return (last / prior - 1.0) * 100.0

    r1d = pct_return(1)
    r5d = pct_return(5)
    r21d = pct_return(21)
    r63d = pct_return(63)

    # 63-day annualized volatility: stdev of daily log returns over the last
    # 63 trading days (i.e. 63 log-return observations, needing 64 closes).
    window = closes[-64:]
    log_returns = [math.log(window[i] / window[i - 1]) for i in range(1, len(window))]
    vol63 = statistics.stdev(log_returns) * math.sqrt(252) * 100.0

    return {
        "close": last,
        "r1d": r1d,
        "r5d": r5d,
        "r21d": r21d,
        "r63d": r63d,
        "vol63": vol63,
    }


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    per_ticker_rows = {}
    for ticker in TICKERS:
        print(f"fetching {ticker}...", file=sys.stderr); time.sleep(1.5)
        raw = fetch_csv(ticker)
        (DATA_DIR / f"{ticker}.yahoo.json").write_text(raw, encoding="utf-8")
        per_ticker_rows[ticker] = parse_rows(ticker, raw)

    # Determine the common as-of date: the latest date present across all
    # tickers. If a ticker has dates beyond that, drop those later rows.
    last_dates = [rows[-1][0] for rows in per_ticker_rows.values()]
    common_date = min(last_dates)
    if len(set(last_dates)) > 1:
        print(
            f"note: last dates differ across tickers ({sorted(set(last_dates))}); "
            f"using common as_of date {common_date}",
            file=sys.stderr,
        )

    instruments = {}
    for ticker in TICKERS:
        rows = per_ticker_rows[ticker]
        # Drop rows after the common date.
        trimmed = [r for r in rows if r[0] <= common_date]
        if not trimmed or trimmed[-1][0] != common_date:
            raise RuntimeError(
                f"{ticker}: does not have a row for common as_of date {common_date}"
            )
        if len(trimmed) < MIN_ROWS:
            raise RuntimeError(
                f"{ticker}: only {len(trimmed)} rows after trimming to {common_date}, "
                f"need at least {MIN_ROWS}"
            )
        closes = [c for _, c in trimmed]
        stats = compute_stats(closes)
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
        "as_of": common_date,
        "instruments": instruments,
        "current_portfolio": CURRENT_PORTFOLIO,
    }

    out_path = DATA_DIR / "snapshot.json"
    out_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out_path} (as_of={common_date})", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
