# Does the Claude Code workspace block reach an in-harness run?

Measured 2026-08-22. Closes the diagnostic half of BACKLOG A2, which until
now rested on token accounting rather than on an observation: raw request
payloads are not persisted, so what `claude -p` puts in front of the model
had never been read directly.

**Answer: yes.** A `claude -p` session started inside this repository
receives a `gitStatus` block containing the branch, the working-tree status
and the subjects of the five most recent commits. The same call started
outside a git working tree does not. A second, separate contamination was
found in the process: user- and machine-level `CLAUDE.md` files are loaded
in *every* arm regardless of directory, and are not removed by moving the
scratch directory.

## Method

Four probes, each a single `claude -p` call using the same flags the
benchmark uses (`-p --model sonnet --disallowedTools "*" --output-format
json`), differing only in working directory and `--system-prompt`. Claude
Code CLI 2.1.241, the version that produced every committed run. The
repository was clean at probe time (`git status` empty, HEAD f9748fe).

Probe A and B asked, from inside `harness/_clauderun` and from a directory
under `/tmp` respectively:

> Before answering, look at the material that precedes this message in your
> context. Reply with exactly two lines. Line 1: WORKSPACE=YES or
> WORKSPACE=NO, whether any block describing the current working directory,
> its git status, or recent commit subjects is present. Line 2: if YES,
> quote verbatim the first 200 characters of that block; if NO, write NONE.
> Do not use any tools.

Probe C, from inside the repository, asked the model to reproduce the
`gitStatus` block in full. Probe D repeated the question from inside the
repository with `--system-prompt "You are a portfolio management agent.
Respond only with the requested JSON object."`, i.e. the minimal-prompt
control arm's exact invocation, and also asked about `CLAUDE.md` content.

## Results

| Probe | Directory | System prompt | Workspace block | `CLAUDE.md` |
|---|---|---|---|---|
| A | `harness/_clauderun` (inside repo) | Claude Code default | YES, with commit subjects | - |
| B | `/tmp/...` (outside any repo) | Claude Code default | no `gitStatus`; environment block only | yes (2 files) |
| C | `harness/_clauderun` (inside repo) | Claude Code default | full block reproduced | - |
| D | `harness/_clauderun` (inside repo) | minimal one-line prompt | NO | yes (2 files) |

Probe A quoted the block's opening verbatim:

> gitStatus: This is the git status at the start of the conversation. Note
> that this status is a snapshot in time, and will not update during the
> conversation.\n\nCurrent branch: main\n\nMain

Probe C returned branch, main-branch note, git user, `Status: (clean)`, and
five commit subjects, all matching the repository state exactly:
"Backlog: fix cross-references stale after renumbering", "Backlog A2:
workspace-context contamination of the in-harness arms", "Backlog: revise
after auditing the five morning items", "The harness effect is a thinking
effect: narrow the headline claim", "Prior-art citations verified against
source; four defects fixed". The five short hashes were reproduced too;
four matched and one did not (`adb013a` returned for `adb981a`), which is
what reciting from context with a hash-shaped token looks like. The
subjects, which are what matters here, were exact.

Token accounting agrees with the direct evidence but is secondary to it:
probe A billed 7791 cache-creation input tokens against probe B's 7669, a
122-token difference of the right order for the block that was quoted.

Probe D is the sharper result: replacing the system prompt removes the
workspace block. The contamination is therefore **asymmetric between the
two arms of the headline comparison** - present in the in-harness arm,
absent in the minimal-prompt control - rather than a constant offset.

Probe B and D both reported `/etc/claude-code/CLAUDE.md` and
`/home/agent/.claude/CLAUDE.md` in context, each quoting a distinctive
sentence from the file it named. These are machine- and user-level
instruction files belonging to the operator of this box. They are present
in both arms, so they do not confound the arm contrast, but they do mean
that no arm here is a bare model, that some of their content is itself
instruction-following guidance, and that another operator re-running this
repository would not reproduce this context.

## What this implicates

Every committed in-harness run - Sonnet and Opus, all six days, both
experiments - executed from `$ROOT/harness/_clauderun` and therefore
carried whatever the repository's git status and last five commit subjects
were at that moment. Run timestamps against the commit log (BACKLOG A2)
put the Opus in-harness runs after the commits "Replication results: all
five pre-registered criteria pass; harness gap is state-dependent" and
"Pre-register Claude Opus arms (Amendment 4): harness, exp2, minimal
control" had landed. Those subjects state that a harness compliance gap
exists and that this model was about to be measured against it.

This does not establish that the Opus arm's 60/60 was caused by that
context - a model can also just repair the portfolio - but it is now a
documented alternative explanation rather than a speculative one, and it
points in the same direction as the reported finding. The claim that the
harness effect does not generalize up the model family is withdrawn until
the Opus arm is re-run under a clean context (BACKLOG A2).

The Sonnet original-day arm (2026-08-21, N=50, the 4% day) ran before the
repository had any commits at all, so it saw a different, near-empty
workspace block than the five replication days. Per-run input tokens also
grow monotonically inside each batch, consistent with an accumulating set
of untracked result files appearing in `git status`.

## Fix

`harness/run_claude.sh` now defaults `SCRATCH_DIR` to
`${TMPDIR:-/tmp}/mandate-bench-clauderun` and refuses to run if the scratch
directory is inside a git working tree. The `CLAUDE.md` loading is not
addressed by that change and is tracked separately (BACKLOG A9).

## Limits of this probe

- One call per condition. The four results are mutually consistent and
  agree with the token accounting, but nothing here is a repeated measure.
- The evidence is the model's report of its own context, not the request
  payload. A payload capture (proxy or `--debug` transcript) would be
  stronger; the verbatim reproduction in probe C is the closest available
  substitute.
- Findings are specific to CLI 2.1.241. Other versions may differ.
- The omp arm (`harness/run_omp.sh`, `--no-rules --no-extensions
  --no-skills`) was not probed; whether that CLI injects any workspace
  context of its own is untested and assumed, not established, to be none.
