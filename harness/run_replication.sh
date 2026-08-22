#!/usr/bin/env bash
# Multi-snapshot replication driver (METHODOLOGY.md Amendment 3,
# METHODOLOGY-EXP2.md Amendment 1). Runs, per replication day:
#   exp1  : 6 models x N on prompts/repl/<d>/prompt.txt      -> results-repl/<d>/
#   exp2  : 6 models x N on prompts/repl/<d>/prompt_exp2.txt -> results-repl-exp2/<d>/
#   exp2ctl: claude + minimal system prompt x N              -> results-repl-exp2ctl/<d>/
# Sequential batches; resumable (both run scripts skip existing outputs).
#
# Usage: run_replication.sh [N per model per day, default 10]

set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
N="${1:-10}"
DAYS=(2026-08-14 2026-08-17 2026-08-18 2026-08-19 2026-08-20)
OMP_MODELS=(
    "google-antigravity/gemini-3.1-pro:high"
    "google-antigravity/gemini-3.7-flash:high"
    "synthetic/syn:large:text:high"
    "synthetic/syn:large:vision:high"
    "synthetic/syn:small:vision:high"
)
MINIMAL_SYSTEM_PROMPT="You are a portfolio management agent. Respond only with the requested JSON object."

for d in "${DAYS[@]}"; do
    p1="$ROOT/prompts/repl/$d/prompt.txt"
    p2="$ROOT/prompts/repl/$d/prompt_exp2.txt"
    [ -s "$p1" ] && [ -s "$p2" ] || { echo "missing prompts for $d" >&2; exit 1; }

    echo "=== $d exp1 ===" >&2
    PROMPT_FILE="$p1" RESULTS_DIR="$ROOT/results-repl/$d/claude-sonnet" \
        bash "$ROOT/harness/run_claude.sh" "$N" 4
    for m in "${OMP_MODELS[@]}"; do
        PROMPT_FILE="$p1" RESULTS_BASE="$ROOT/results-repl/$d" \
            bash "$ROOT/harness/run_omp.sh" "$m" "$N" 2
    done

    echo "=== $d exp2 ===" >&2
    PROMPT_FILE="$p2" RESULTS_DIR="$ROOT/results-repl-exp2/$d/claude-sonnet" \
        bash "$ROOT/harness/run_claude.sh" "$N" 4
    for m in "${OMP_MODELS[@]}"; do
        PROMPT_FILE="$p2" RESULTS_BASE="$ROOT/results-repl-exp2/$d" \
            bash "$ROOT/harness/run_omp.sh" "$m" "$N" 2
    done

    echo "=== $d exp2 control ===" >&2
    PROMPT_FILE="$p2" SYSTEM_PROMPT="$MINIMAL_SYSTEM_PROMPT" \
        RESULTS_DIR="$ROOT/results-repl-exp2ctl/$d/claude-sonnet-minimal" \
        bash "$ROOT/harness/run_claude.sh" "$N" 4
done

echo "run_replication.sh: all days done" >&2
