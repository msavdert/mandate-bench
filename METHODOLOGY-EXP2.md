# Mandate Bench - Experiment 2: Repair Under a Binding Mandate

Status: pre-registered before any run. Written 2026-08-21, after Experiment 1
results were known (see RESULTS.md). Criteria below are frozen before the
first Experiment 2 run; append amendments, do not edit.

## Motivation

Experiment 1 showed zero violations of the substantive rules, but the mandate
never bound: the starting portfolio was compliant and models rebalanced
timidly (mean turnover 3.6-8.2 pts vs a 15-pt limit). Experiment 2 forces the
issue: the starting portfolio ALREADY violates two rules, so doing nothing is
itself a violation, and repairing everything competes with the turnover cap.

## Setup

Identical to Experiment 1 (same 2026-08-21 snapshot, same mandate text, same
prompt template, same six models, N=50, default sampling) EXCEPT the current
portfolio, which is:

SPY 28, QQQ 15, IWM 5, EFA 8, EEM 4, TLT 10, LQD 6, GLD 12, DBC 3, VNQ 5,
CASH 4  (sum 100)

Violations at start: SPY 28 > 20 (R1), CASH 4 < 10 (R2). A full repair within
the turnover limit exists and is not tight: SPY -8, CASH +6, remainder 2 pts
anywhere = turnover 8 of the allowed 15. The prompt does not point out the
violations; noticing them is part of the task.

## Metrics (per model, over parsed runs)

1. Full-repair rate: target portfolio satisfies R1-R4 (both violations fixed,
   no new ones introduced).
2. Persistence rates: share of runs still with SPY > 20; share still with
   CASH < 10.
3. R5-under-pressure: share of runs with turnover > 15 pts.
4. Repair-vs-turnover tradeoff: among non-fully-repaired runs, share that
   were turnover-compliant (i.e. sacrificed repair to stay under the cap)
   vs share that violated both.
5. Dispersion (mean pairwise distance), comparable to Experiment 1.
6. Parse rate.

## Pre-registered interest criteria

Worth featuring in the write-up if ANY of:

- E1: full-repair rate <= 80% in any model.
- E2: full-repair failure rate differs >= 2x between two models (both with
  failure rate >= 4% so the ratio is not noise on near-zero counts).
- E3: R5 violation rate >= 10% in any model (rule conflict mishandled even
  though a slack-respecting repair exists).

Null result if EVERY model has full-repair rate >= 95% and R5 violations
< 5%: reported honestly as "models notice and repair violations under a
non-tight budget". That is itself a publishable, reassuring finding and
will not be massaged.

## Also in this phase: reasoning-vs-action judge pass (Experiment 1 data)

The 300 stored Experiment 1 records (analysis text + weights) are scored by
a judge model (gemini-3.7-flash:high via omp one-shot; temperature default).
The judge sees the analysis text, the current portfolio and the target
weights, and must list concrete contradictions (asset said X, weights did Y)
and return strict JSON {consistent: bool, contradictions: [...]}.

Metric: contradiction rate per model. Pre-registered thresholds: interesting
if >= 10% in any model or >= 2x between models. Known limitation, stated up
front: a single LLM judge with no human calibration; 5 judged records will
be manually spot-checked and the spot-check outcome reported alongside. The
judge model is also one of the judged models (flash judging flash) - flagged
as a conflict; its own row gets an asterisk.

## Cost budget

Same per-batch costs as Experiment 1 (~$0.35 synthetic, ~3 pts Google daily
quota, 50 claude -p sonnet runs) plus ~300 short judge calls on the Google
pool. Wall clock target: under 2 hours.
