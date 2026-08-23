#!/usr/bin/env bash
# Run N mandate-bench decisions through Claude Code headless mode.
#
# Usage: run_claude.sh <N> [concurrency, default 4]
#
# For i in 1..N, skips results/claude-sonnet/run_<i>.json if it already
# exists (resumable). Each run pipes prompts/prompt.txt into `claude -p`
# from inside a scratch directory OUTSIDE this repository, and writes the
# raw --output-format json response to results/claude-sonnet/run_<i>.json.
#
# The scratch directory must be outside the repository. Until 2026-08-22 it
# was $ROOT/harness/_clauderun, on the assumption that an empty directory
# prevents context pickup. It does not: an empty directory prevents a
# project CLAUDE.md from loading, but Claude Code still injects a workspace
# block for any session started inside a git repository, carrying the
# branch, git status and the most recent commit subjects. That was measured
# on 2026-08-22 (research/harness-context-probe.md) and the affected runs
# are recorded in METHODOLOGY.md Amendment 5. Note that user- and
# machine-level CLAUDE.md files are loaded regardless of directory and are
# NOT removed by this change.
#
# Notes on flags (checked against `claude -p --help` / `claude --help` on
# this machine before writing this script):
#   -p --output-format json   headless mode, single JSON result object
#   --model sonnet             pin the model
#   --disallowedTools "*"      deny all tools (this install has no
#                               --max-turns flag; the prompt's own "do not
#                               use any tools" instruction plus this flag is
#                               the closest available substitute for capping
#                               the run to a single turn)

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROMPT_FILE="${PROMPT_FILE:-$ROOT/prompts/prompt.txt}"
RESULTS_DIR="${RESULTS_DIR:-$ROOT/results/claude-sonnet}"
# MODEL (optional, METHODOLOGY.md Amendment 4): claude model to pin.
# Unset, behavior is identical to the original experiments.
MODEL="${MODEL:-sonnet}"
# Outside the repository on purpose - see the header. Overridable, but any
# override must also be outside a git working tree.
SCRATCH_DIR="${SCRATCH_DIR:-${TMPDIR:-/tmp}/mandate-bench-clauderun}"

N="${1:?usage: run_claude.sh <N> [concurrency]}"
CONCURRENCY="${2:-4}"

if [[ ! -f "$PROMPT_FILE" ]]; then
    echo "ERROR: $PROMPT_FILE not found; run build_prompt.py first" >&2
    exit 1
fi

mkdir -p "$RESULTS_DIR" "$SCRATCH_DIR"

# Guard against the 2026-08-22 defect returning: a scratch directory inside a
# git working tree makes Claude Code inject that repository's branch, status
# and recent commit subjects into every run.
if (cd "$SCRATCH_DIR" && git rev-parse --is-inside-work-tree >/dev/null 2>&1); then
    echo "ERROR: SCRATCH_DIR ($SCRATCH_DIR) is inside a git working tree." >&2
    echo "       Workspace context would leak into every run; pick a path outside." >&2
    exit 1
fi

run_one() {
    local idx="$1"
    local padded
    padded=$(printf "%03d" "$idx")
    local out_file="$RESULTS_DIR/run_${padded}.json"

    if [[ -f "$out_file" ]]; then
        echo "run ${padded} skipped (exists)" >&2
        return 0
    fi

    local tmp_file
    tmp_file=$(mktemp "$SCRATCH_DIR/run_${padded}.XXXXXX.json")

    # SYSTEM_PROMPT (optional, METHODOLOGY-EXP2.md Amendment 1): replaces the
    # Claude Code system prompt for the minimal-prompt control arm. Unset,
    # the invocation is unchanged from the original experiments.
    local extra_args=()
    if [[ -n "${SYSTEM_PROMPT:-}" ]]; then
        extra_args+=(--system-prompt "$SYSTEM_PROMPT")
    fi

    if (cd "$SCRATCH_DIR" && claude -p --output-format json --model "$MODEL" \
            --disallowedTools "*" "${extra_args[@]}" \
            < "$PROMPT_FILE" > "$tmp_file" 2>"${tmp_file}.err"); then
        mv "$tmp_file" "$out_file"
        rm -f "${tmp_file}.err"
        echo "run ${padded} done" >&2
    else
        echo "run ${padded} FAILED (see ${tmp_file}.err)" >&2
        rm -f "$tmp_file"
    fi
}

pids=()
running=0
for ((i = 1; i <= N; i++)); do
    run_one "$i" &
    pids+=($!)
    running=$((running + 1))
    if (( running >= CONCURRENCY )); then
        wait -n
        running=$((running - 1))
    fi
done

wait

echo "run_claude.sh: done ($N requested)" >&2
