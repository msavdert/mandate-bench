# Backlog

Open work items, most blocking first.

Revised 2026-08-22, after auditing the five items raised earlier the same
day. Updated later that day: A2's diagnostic ran and confirmed the defect,
A3 is closed, and the CLAUDE.md contamination it surfaced is now A9. The audit changed the picture enough that the old numbering is not
worth preserving; what the previous items got right, got wrong, and missed
is recorded under "Disposition of the 2026-08-22 morning items" at the
bottom, and the corrections that closed them are already in the tree.

The short version: the two items that were marked publication-blocking were
correctly prioritised and wrongly diagnosed. The prior-art citations turned
out to be real. The prompt-delivery confound turned out to be refutable from
data already committed. And the actual trivial explanation for the headline
result was named by neither item: the harness arm largely did not use
extended thinking, and repair is almost perfectly predicted by that. That
finding is now in the report; the experiment that would make it causal is
item A1 below. Auditing the harness invocation for that item then surfaced a
second blocker, A2: the in-harness arm runs from a scratch directory inside
this repository, so the workspace context Claude Code injects - git status
and recent commit subjects - differed between arms and across days, in a
direction that tracks the results.

---

## A1. Run the thinking-forced harness arm

**Status:** open, blocking publication. Needs new runs.

The whole result now rests on a mediator identified observationally. Within
the Sonnet in-harness arm, runs with zero thinking tokens repaired 0/75 and
runs with thinking tokens repaired 19/25; the minimal-prompt control, where
thinking ran in 60/60, repaired 45/60. Conditional on thinking, the two arms
are indistinguishable. That is a strong association across 160 runs, but it
is an association: nothing in the repo forces the thinking level on either
side, so "the harness suppresses thinking" and "the states where the model
does not think are also the states where it would not have repaired anyway"
are both consistent with it.

**Why this is first:** every other claim in the report is now phrased around
the mediator. If forcing thinking inside the harness does not close the gap,
the mediator is a correlate rather than a mechanism and the interpretation
has to change again. It is one cheap arm, not a redesign.

**Done when:** an in-harness arm with extended thinking forced on has been
run over the same six snapshots at the same N, pre-registered as an
amendment before it runs, with a stated prediction (repair rate should reach
the 75-76% conditional rate, not the 19% pooled rate). Report the result
whichever way it falls. A second, cheaper diagnostic is worth running at the
same time: whether the harness system prompt itself suppresses thinking, by
varying only that while holding the task prompt fixed.

Since 2026-08-22 the arm will run under the corrected scratch path (A2), so
it is not context-identical to the committed in-harness runs. Say so when
comparing; ideally re-run a plain in-harness arm alongside it so the
thinking-forced condition has a clean-context baseline of its own.

## A2. Rule out workspace-context contamination of the in-harness arms

**Status:** diagnosed and fixed 2026-08-22; still open and still blocking
publication, because the Opus arm has not been re-run.

**Confirmed.** Four probes (research/harness-context-probe.md) established
directly, not by inference, that a `claude -p` session started inside this
repository receives a `gitStatus` block with branch, working-tree status and
the five most recent commit subjects; that a session started outside a git
tree does not; and that the minimal-prompt control's `--system-prompt`
override removes the block. The contamination is therefore asymmetric
between the two arms of the headline comparison. A second contamination was
found in the process and is tracked separately as A9.

**Done since:** `SCRATCH_DIR` now defaults outside the repository and
`run_claude.sh` refuses to start inside a git working tree; METHODOLOGY.md
Amendment 5 records the defect and its scope; the family-non-generalization
claim is withdrawn from README.md, RESULTS.md, docs/index.html, report.html
and data/leaderboard.json.

**Still to do:** re-run the Opus arm (three arms x six days x N=10) under
the clean context and report whichever way it falls. Until then the
withdrawal stands.

`harness/run_claude.sh:30` sets `SCRATCH_DIR="$ROOT/harness/_clauderun"`,
inside this repository's working tree. Claude Code injects a workspace
context block for a session started in a git repository, including git
status and recent commit subjects. The script's header comment claims an
empty scratch directory prevents context pickup; an empty directory prevents
a project `CLAUDE.md` from loading, not the repository state around it.

Two consequences, both aligned with the results rather than orthogonal to
them.

**The Opus arm may have been told what it was being tested for.** Run
timestamps against the commit log:

| Arm | ran | most recent commit subjects then visible |
|---|---|---|
| Sonnet exp2, 2026-08-21, N=50 | 08-21 21:03 | none; first commit landed 21:48 |
| Sonnet exp2, five replication days | 08-21 22:15-23:27 | "Pre-register multi-snapshot replication (5 market days, exp1 + exp2 + control)" |
| Opus exp2, both arms, six days | 08-21 23:54 - 08-22 00:05 | "Replication results: all five pre-registered criteria pass; harness gap is state-dependent", "Pre-register Claude Opus arms (Amendment 4): harness, exp2, minimal control" |

If the workspace block reaches the model, the Opus in-harness runs carried,
in context, a statement that a harness compliance gap exists and that this
model was about to be measured against it. That is a live alternative
explanation for 60/60, and it points the same way as the finding, which is
the direction that should worry us most.

**The headline 4% day had a different workspace context from the other
five.** The original N=50 arm ran before the repository had any commits, and
it carries the lowest in-harness input-token count of the six days (11812
against 12035-12118). Per-run input tokens also grow monotonically within
each batch, which is what an accumulating set of untracked result files in
`git status` looks like. So "the same harness" was not the same across days,
and the day that differs most is the day the headline number comes from.

Neither point is established: raw request payloads are not persisted, so
whether `claude -p` includes the workspace block in this CLI version
(2.1.241) is inferred from token accounting, not observed.

**Done when:** the Opus arm has been re-run under the corrected scratch
path and reported. If the clean-context Opus arm still repairs at or near
60/60, the family-non-generalization claim comes back, with the re-run as
its evidence; if it does not, the claim was an artifact and the report says
so.

## A3. Unify the repair-metric definition

**Status:** closed 2026-08-22.

Canonical definition, recorded as METHODOLOGY.md Amendment 6: a run is a
full repair if it is usable and violates none of R1-R5. `analyze.py` holds
the single definition (`REPAIR_RULES`, `is_full_repair`), writes a
`full_repair` column into `parsed.csv` and a per-model line into
`summary.md`; `replication_report.py` imports the same constant. All 18
per-directory `parsed.csv`/`summary.md` pairs and the replication report
were regenerated; a field-by-field diff confirms nothing moved except the
new column, the new summary line, and the intended rate changes.

What changed: only R3 is ever violated in the committed data (17 runs, zero
R4, zero R5), so R1-R4 and R1-R5 coincide here and the real change is
R1+R2 -> all-rules. Replication exp-2 open-weights rows drop to 94%, 96%,
96% (REP2-B range 98-100% -> 94-100%); every Claude figure is unchanged,
and all five pre-registered criteria keep their verdicts. Restated figures
are tabulated in RESULTS.md under "Repair metric".

Two things found while doing it: `results-repl/REPLICATION.md` had never
been regenerated after the Amendment 4 Opus arms landed and was missing
them, and REP2-B's "every omp model" filter was written as "not the two
Sonnet arms", which would have silently scored the Opus rows against an
omp-only criterion. Both fixed.

## A4. Pin sampling settings before ranking dispersion across models

**Status:** open. Needs new runs.

`METHODOLOGY.md:22` records that temperature is not pinned. The 2.7x
dispersion spread therefore mixes model behaviour with each provider's
default sampling configuration, and the Claude row additionally reached the
model through a different access path than the other five. The README
caveat covers the temperature-versus-instability conflation but not the
narrower point that a *cross-model ratio* on this metric is confounded by
provider defaults, so the ranking is not a model comparison.

**Done when:** either the dispersion arm is re-run with temperature and
top-p pinned to the same values everywhere and one access path, or the
cross-model ratio is withdrawn as a ranking and reported per model as a
deployed-defaults observation.

## A5. Measure judge recall before the contradiction rate is used for anything

**Status:** open.

Three judge positives were hand-verified; zero negatives were audited. There
is no calibration set (`README.md` lists one only as future work). Two
independent probes of the Gemini rows found no unflagged contradictions,
which is reassuring but is not a recall estimate.

There is also a style confound that no amount of judge re-running fixes:
models whose rationales make fewer checkable numeric commitments score
better by construction. Over 50 runs, one model made 18 explicit delta
claims and 5 "held flat" claims where another made 14 and 28. A contradiction
rate that is not normalised by the number of falsifiable claims is partly a
measure of prose vagueness.

**Done when:** a hand-labelled calibration set exists with precision and
recall reported for the judge, the rate is normalised per checkable claim,
and a cross-family judge is used so no model scores its own outputs. Until
all three hold, the measurement stays out of any ranking.

## A6. Make day-level clustering the pre-registered unit for future arms

**Status:** open for the next pre-registration. The existing analysis is
already corrected in the tree.

Pooled replication rates treated 50 runs as 50 independent draws when the
market day is the sampling unit and day effects are enormous (per-day
in-harness repair spans 0-90%). The day-level paired test, now reported as
primary in RESULTS.md, gives mean +42 points with t(4) = 2.64 and p = 0.058
over the five replication days, and +46 points with p = 0.020 over all six.
Pre-registered criterion REP2-C ("at least 30 points") therefore passes on
the pooled-run analysis but not, at conventional thresholds, on the analysis
that respects clustering. The Opus-versus-Sonnet contrast survives it
comfortably (p about 0.006).

**Done when:** the next pre-registration names the market day as the
sampling unit, states the paired test as the primary analysis, and sets the
number of days from a power calculation rather than from convenience. Five
days cannot support a 30-point criterion at conventional power.

## A7. Finish the repositioning as a technical report

**Status:** open, do after A1 and A2.

The README now leads with the harness-times-thinking finding and the
leaderboard is split into two tables that no longer invite row-for-row
comparison across different N, access paths and time bases. What remains is
the larger move the previous B5 argued for and which is still right: this is
not a general-purpose instruction-following benchmark and should not be
pitched against IFEval or FollowBench, where it loses on scale, adoption and
breadth with no path to winning. Its contribution is one result about agent
harnesses that production systems care about and that no surveyed benchmark
isolates.

That case is stronger on internal evidence than on the external critique
that prompted it. Of the three findings in the original abstract, only the
harness effect has both a large effect size and a pre-registered
replication: experiment 1's half of finding (1) is a null, finding (2) is
confounded by A4, and finding (3) is underpowered per A5.

**Done when:** the material is restructured as a short technical report
about the harness result, with the benchmark harness presented as its
reproducibility appendix rather than as a candidate leaderboard standard.

## A8. Citation housekeeping

**Status:** open, low priority. Not a publication blocker.

`research/prior-art-verification.md` now records a direct fetch of every
identifier in `research/prior-art.md`, performed 2026-08-22, and supersedes
the five-line summary in `research/prior-art-run.log`. All 13 arXiv IDs
resolve to real papers whose titles and dates match. Four defects were found
and fixed: a wrong date and an incomplete author list on arXiv:2508.18427, a
dead GitHub URL removed, a GitHub URL whose repository describes a different
artifact than the paper removed, and a truncated title corrected.

Two loose ends remain. SSRN DOI 10.2139/ssrn.5189069 returns HTTP 403 behind
a bot block, so it is attested only through the paper's verified arXiv
mirror. And the FinPersona-Bench row claims repository activity in July 2026
without a fetched commit timestamp behind it.

**Done when:** the SSRN entry is confirmed by some route that is not
blocked, or replaced by the arXiv mirror; and every "activity" cell is
either backed by a fetched commit date or dropped from the table.

## A9. Operator CLAUDE.md files are in every Claude run

**Status:** open, not a publication blocker for the arm contrast; is one
for reproducibility claims.

Found while probing A2. `/etc/claude-code/CLAUDE.md` (machine policy) and
`/home/agent/.claude/CLAUDE.md` (the operator's global preferences) are
loaded into every `claude -p` session regardless of working directory, and
the `--system-prompt` override does not remove them: both the in-harness
and the minimal-prompt control arm ran with them in context. Each was
confirmed by name and by a quoted sentence in
research/harness-context-probe.md.

Because it is common to both arms it does not confound the harness contrast.
It does mean no arm here is a bare model, that part of what was in context
is itself instruction-following guidance, and that nobody else re-running
this repository reproduces the same context - which is a problem for a
benchmark whose whole point is that context changes behaviour.

**Done when:** the Claude arms run with a controlled instruction-file
context - most likely by pointing `HOME` at the scratch directory and
checking with the same probe that neither file is present, with whatever
remains loaded documented verbatim in METHODOLOGY.md. Whether a `HOME`
override actually suppresses the machine-level file is untested. Whichever
runs are used for publication should be collected under that controlled
context, so this is worth settling before A1 and the A2 Opus re-run rather
than after.

---

## Disposition of the 2026-08-22 morning items

Recorded because the errors are instructive, not for bookkeeping.

**Old B1, verify every citation - closed, hypothesis refuted.** Every arXiv
ID in `prior-art.md` was resolved directly against arxiv.org. None was
fabricated; the 2026 identifiers that looked suspicious are real papers with
matching titles and dates. The item was right that unverified citations were
carrying the novelty claim and right that closing it was cheap. It was wrong
to rank this first: the reputational risk it feared did not exist, and the
four real defects it would have caught are footnote-scale. Residue is A8.

**Old B2, rule out the trivial explanation - closed as ruled out, but it
named the wrong confound.** Its hypothesis was that the two arms received
different prompt bytes. Both arms read the same prompt file from the same
script (`harness/run_claude.sh:25,64-66`); 42 of 50 harness runs quote
two-decimal figures that appear only in the prompt, and every run emits the
required 11-key JSON, so the prompt arrived intact head, middle and tail.
Raw request payloads are not persisted, so a literal byte diff remains
impossible in-repo and the token accounting stands in for it.

The item's instinct - that a surprisingly strong result is a bug hypothesis
first - was correct and was vindicated, just not where it pointed. The
actual explanation was in the persisted `thinking_tokens` field the whole
time. Nine other candidate confounds were checked and ruled out in the same
pass (truncation, model-snapshot drift, parse failures scored as
non-repairs, retries, tool routing, cross-run state); two remain open and
are now A1 and A4.

One further error the item did not catch: the "3.6 versus 8.0-10.7 turnover"
row it cited as its evidence compares Sonnet against four models reached
through a different CLI, with a different system prompt, a different
delivery mechanism and a reasoning-effort suffix in their model IDs. That
row should not be read as one model measured two ways.

**Old B3, narrow the headline claim - done, and the item itself repeated the
error it was fixing.** It cited "Opus 5: 120/120 in the identical harness",
which conflates 60 in-harness runs with 60 minimal-prompt control runs. That
wording had propagated into `README.md` and `docs/index.html`; all three are
now corrected to 60/60 plus 60/60. The claim is now stated at the same
altitude in the README, RESULTS.md and the Pages site, and the harness runs
were not equally sized either: Opus carried 6.7-7.2k input tokens against
Sonnet's 11.8-12.1k on the same days.

**Old B4, remove the contradiction column - done, remedy (b), but the
diagnosis was incomplete.** The column is gone from the leaderboard in both
the README and the Pages site and survives in RESULTS.md as a scoped
observation. The conflict of interest was real but was not the disqualifying
problem: at N=50 the column has no resolving power at all (0/50 against
5/50 is Fisher p = 0.056, and every row's interval contains every other's),
and the style confound in A5 means a cross-family judge would have shipped a
re-ranked column that still could not separate 8% from 10%. Remedy (a) would
have looked like a fix and would not have been one.

**Old B5, reposition the repository - partly done, continues as A6.**
Verified and understated: the leaderboard mixed three values of N, three
access paths rather than two, and two time bases, and set Sonnet's worst
single day against Opus's six-day pooled figure. All of that is now split
into two separate tables with the matched 19/100 Sonnet figure alongside the
Opus rows.

**Missed by all five items:** day-level clustering (A6), the three
incompatible repair-metric definitions (A3), the absence of any committed
code behind the published bootstrap CIs (now `harness/bootstrap_ci.py`, and
all seven published intervals reproduce), a stale `data/leaderboard.json`
(regenerated), and the post-hoc provenance of the original minimal-prompt
control, which `METHODOLOGY-EXP2.md` never pre-registered and which
`RESULTS.md` described as "pre-planned as a follow-up".
