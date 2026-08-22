#!/usr/bin/env bash
# Run N repeats of the frozen mandate-bench prompt against one model via the
# omp CLI in one-shot mode (no tools, no session, minimal system prompt).
#
# Usage: run_omp.sh <model> <N> [concurrency]
#   model        e.g. synthetic/syn:small:vision:high
#   N            number of runs
#   concurrency  parallel omp processes, default 2
#
# Output: results/<slug>/run_<i>.txt (raw omp stdout, the assistant text).
# Failures leave run_<i>.err and no .txt; the batch continues. Resumable:
# existing non-empty .txt files are skipped.

set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROMPT="${PROMPT_FILE:-$ROOT/prompts/prompt.txt}"
SYSTEM_PROMPT="You are a portfolio management agent. Respond only with the requested JSON object."

MODEL="${1:?usage: run_omp.sh <model> <N> [concurrency]}"
N="${2:?usage: run_omp.sh <model> <N> [concurrency]}"
CONC="${3:-2}"

[ -s "$PROMPT" ] || { echo "missing $PROMPT" >&2; exit 1; }

SLUG="$(echo "$MODEL" | tr '/:' '--')"
OUTDIR="${RESULTS_BASE:-$ROOT/results}/$SLUG"
mkdir -p "$OUTDIR"

run_one() {
    local i="$1"
    local pad
    pad="$(printf '%03d' "$i")"
    local out="$OUTDIR/run_$pad.txt"
    local err="$OUTDIR/run_$pad.err"
    if [ -s "$out" ]; then
        echo "[$SLUG] run $pad exists, skipping" >&2
        return 0
    fi
    if timeout 180 omp -p --no-tools --no-session --no-skills --no-rules \
        --no-extensions --system-prompt "$SYSTEM_PROMPT" \
        --model "$MODEL" @"$PROMPT" >"$out.tmp" 2>"$err.tmp"; then
        if [ -s "$out.tmp" ]; then
            mv "$out.tmp" "$out"
            rm -f "$err.tmp" "$err"
            echo "[$SLUG] run $pad ok" >&2
        else
            mv "$err.tmp" "$err"
            rm -f "$out.tmp"
            echo "[$SLUG] run $pad EMPTY output" >&2
        fi
    else
        local rc=$?
        mv "$err.tmp" "$err"
        rm -f "$out.tmp"
        echo "[$SLUG] run $pad FAILED rc=$rc" >&2
    fi
}

active=0
for i in $(seq 1 "$N"); do
    run_one "$i" &
    active=$((active + 1))
    if [ "$active" -ge "$CONC" ]; then
        wait -n
        active=$((active - 1))
    fi
    sleep 1
done
wait
done_count="$(find "$OUTDIR" -name 'run_*.txt' -size +0c | wc -l)"
echo "[$SLUG] batch done: $done_count/$N outputs present" >&2
