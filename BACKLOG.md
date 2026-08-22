# Backlog

Open work items, most blocking first. Items B1 and B2 are pre-publication
blockers: neither the report nor the Pages site should be promoted further
until both are closed.

Raised 2026-08-22 during a review of an external critique of the project.
The critique itself argued that mandate-bench is a narrow re-run of
IFEval / FollowBench / HarmBench / AgentBench. That reading is answered
already in `research/prior-art.md` (those benchmarks constrain lexical and
format properties of text; this one constrains a continuous allocation
vector on the simplex) and it misses the actual headline result, which is
not a constraint-following rate at all but a model-times-context effect:
the same model on the same prompt repairs 4% in-harness and 70% under a
minimal system prompt, and the effect does not generalize up the family
(Opus 5: 120/120 in the identical harness). No IFEval-class benchmark can
produce that number, because harness context is not a variable in any of
them. The items below are the parts of the critique that do land, plus
three larger problems it did not raise.

---

## B1. Verify every citation in `research/prior-art.md`

**Status:** open, blocking publication.

`research/prior-art.md` cites arXiv IDs and GitHub repositories with 2026
dates (arXiv:2601.15322, arXiv:2606.31522, arXiv:2608.09988,
arXiv:2605.16895, arXiv:2604.18373, arXiv:2603.00285, arXiv:2608.00991,
and others). The only provenance in the repo is `research/prior-art-run.log`,
which is a five-line subagent summary asserting that "all search queries and
source fetches succeeded". There is no transcript of the fetches themselves,
so no citation in that file is independently verified inside this repository.

**Why this is first:** the prior-art survey is what carries the novelty
claim - the whole "no existing benchmark measures X" argument rests on it.
If any of those identifiers is a hallucinated citation, the novelty claim
collapses and takes the project's credibility with it. This is a larger
reputational risk than anything in the critique, and it is cheap to close.

**Done when:** every arXiv ID, SSRN DOI and GitHub URL in `prior-art.md`
has been resolved and its title/authors/date checked against what the table
claims; unresolvable entries are deleted, not softened; the fetch evidence
is committed alongside the report rather than summarized.

## B2. Rule out the trivial explanation for the harness gap

**Status:** open, blocking publication.

The in-harness Claude arm shows mean turnover 3.6 against 8.0-10.7 for
every one-shot arm (RESULTS.md, experiment 2 table). That is consistent
with the stated interpretation - the agent does not notice it needs to act -
but it is equally consistent with a mundane delivery difference: the harness
run receiving a truncated, reformatted or tool-routed version of the prompt,
so that the two arms are not answering the same question at all.

**Why:** a surprisingly strong result is a bug hypothesis before it is a
finding. "Harness context blinds a model to explicit numeric rules" is the
project's most quotable claim and its most actionable one; it must not rest
on an unaudited assumption that both arms received identical input.

**Done when:** the exact byte sequence the model received in the harness arm
has been captured and diffed against `prompts/`, for at least one repaired
and one unrepaired run; the diff (or its absence) is recorded in RESULTS.md.
If the prompts differ, the finding is rewritten around what actually differs.

## B3. Narrow the headline claim to what the data supports

**Status:** open.

The README abstract attributes the gap to "harness context rather than model
capability". The evidence in hand is narrower on two axes that the repo has
itself already established: the replication found in-harness repair swinging
0-90% across market days, and the Opus arms repaired 120/120 in the identical
harness. The supported claim is therefore closer to: *Claude Sonnet 5, inside
the Claude Code harness, on some market states, fails to act on explicit
numeric mandates it enforces under a minimal system prompt.*

**Why:** the narrower claim is still the interesting one, and it is the one
that survives contact with a skeptical reader. Overreaching in the abstract
invites the reader to discount the parts that are solid. The state-dependence
and the family non-generalization are findings, not caveats, and reading as
if they were buried undersells them.

**Done when:** the README abstract, the RESULTS.md interpretation paragraph
and `docs/index.html` state the claim at the same, narrower altitude, with
day-to-day variance and the Opus null presented as part of the result.

## B4. Remove the contradiction column from the leaderboard

**Status:** open.

The reasoning-contradiction judge is `gemini-3.7-flash:high` and it scored
both Gemini rows at 0.0%. The conflict of interest is disclosed in three
places, which is the right instinct, but a column that is disclosed as
uninterpretable is still sitting in the ranking table on the README and on
the Pages site.

**Why:** a flagged-unusable column in a leaderboard reads as carelessness to
exactly the audience the project needs, and it is the kind of detail that
gets a whole table dismissed. Either fix the measurement or stop ranking on
it; keeping it visible with an asterisk is the one option that gets no credit
for the honesty and pays the full cost of the flaw.

**Done when:** either (a) the pass is re-run with a cross-family judge so no
model scores its own outputs, and the column returns with that judge named,
or (b) the column is dropped from the leaderboard in README.md and
`docs/index.html` and survives only in RESULTS.md as a preliminary, clearly
scoped observation.

## B5. Reposition the repository around its single finding

**Status:** open, do after B1-B4.

The critique is correct that this is not a general-purpose instruction
following benchmark and should not be pitched against IFEval or FollowBench;
as a candidate leaderboard standard it loses on scale, adoption and breadth,
and there is no path where it wins. Its actual contribution is one result
about agent harnesses that production systems care about and that no current
benchmark isolates.

**Why:** the current framing invites the comparison it cannot win, and buries
the comparison it does win. A short technical report built around the
harness result, with the benchmark harness as its reproducibility appendix,
is both more honest about scope and a stronger read than a leaderboard whose
cells were never meant to be compared against each other - three different
values of N and two different access paths currently share one table.

**Done when:** README leads with the harness finding rather than the
leaderboard; the leaderboard is presented as supporting evidence with its
non-comparable cells visually separated rather than footnoted.
