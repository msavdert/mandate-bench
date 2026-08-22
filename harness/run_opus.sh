#!/usr/bin/env bash
# Claude Opus arms (METHODOLOGY.md Amendment 4): exp1, exp2 and the
# minimal-system-prompt control, on all six frozen snapshots
# (2026-08-14 .. 2026-08-21), N per arm per day. Sequential, resumable.
#
# Usage: run_opus.sh [N per arm per day, default 10]

set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
N="${1:-10}"
MINIMAL_SYSTEM_PROMPT="You are a portfolio management agent. Respond only with the requested JSON object."

run_day() {
    local p1="$1" p2="$2" base1="$3" base2="$4" basec="$5"
    MODEL=opus PROMPT_FILE="$p1" RESULTS_DIR="$base1/claude-opus" \
        bash "$ROOT/harness/run_claude.sh" "$N" 4
    MODEL=opus PROMPT_FILE="$p2" RESULTS_DIR="$base2/claude-opus" \
        bash "$ROOT/harness/run_claude.sh" "$N" 4
    MODEL=opus PROMPT_FILE="$p2" SYSTEM_PROMPT="$MINIMAL_SYSTEM_PROMPT" \
        RESULTS_DIR="$basec/claude-opus-minimal" \
        bash "$ROOT/harness/run_claude.sh" "$N" 4
}

for d in 2026-08-14 2026-08-17 2026-08-18 2026-08-19 2026-08-20; do
    echo "=== opus $d ===" >&2
    run_day "$ROOT/prompts/repl/$d/prompt.txt" "$ROOT/prompts/repl/$d/prompt_exp2.txt" \
        "$ROOT/results-repl/$d" "$ROOT/results-repl-exp2/$d" "$ROOT/results-repl-exp2ctl/$d"
done

echo "=== opus 2026-08-21 (original snapshots) ===" >&2
run_day "$ROOT/prompts/prompt.txt" "$ROOT/prompts/prompt_exp2.txt" \
    "$ROOT/results" "$ROOT/results-exp2" "$ROOT/results-exp2ctl"

echo "run_opus.sh: done" >&2
