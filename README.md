# Mandate Bench

Behavioral benchmarking of LLM agents on a fixed portfolio-rebalancing task:
mandate compliance, decision consistency, and reasoning-action agreement.
Deliberately not a returns benchmark.

Report and living leaderboard: https://msavdert.github.io/mandate-bench/

## Abstract

Public AI-trading arenas rank agents by short-horizon profit, a metric
dominated by market noise at any feasible sample size. Mandate Bench instead
measures what an agent *does*: given an identical frozen market snapshot and
an explicit numeric mandate (position cap, cash floor, turnover limit), does
the agent obey the rules, does it make the same decision twice, and does its
stated rationale match its executed trades? In v0.1 (2026-08-21) six models
made 610 decisions across two pre-registered experiments plus one control,
and 300 stored rationales were audited by a judge model. Three findings:
(1) with a rule-violating starting portfolio, five of six models repaired the
violations in 96-100% of runs, while the same task run inside a large
coding-agent harness collapsed to 4% - and recovered to 70% when only the
system prompt was minimized, implicating harness context rather than model
capability; (2) no model is close to run-to-run deterministic at deployed
settings, and dispersion differs 2.7x across models (bootstrap 95% CI on the
ratio: 2.3-3.3); (3) roughly one decision in ten, for three of six models,
directly contradicts its own written rationale.

Update 2026-08-21: a pre-registered replication over five additional market
days (650 new decisions, N=10 per model per day) passed all five of its
pre-registered criteria: the violation null and the dispersion spread
(3.13x pooled) replicate, and the harness gap replicates qualitatively
(34% pooled in-harness repair vs 98-100% one-shot and 76% minimal-prompt
control). The replication's own finding: harness repair swings 0-90% by
market day, so the original 4% sits at the bad end of a wide,
state-dependent range. Details in RESULTS.md and results-repl/REPLICATION.md.

## Leaderboard (v0.1, snapshot 2026-08-21, N=50 per cell)

| Model | Access path | Repair rate (exp 2) | Dispersion, pts (exp 1) | Reasoning contradictions |
|---|---|---|---|---|
| Gemini 3.1 Pro (high) | one-shot API | 100% | 3.65 [3.07, 4.06] | 0%* |
| Gemini 3.7 Flash (high) | one-shot API | 100% | 2.31 [1.96, 2.57] | 0%* |
| Kimi-K3 | one-shot API | 100% | 6.27 [5.50, 6.85] | 8% |
| Qwen3.6-27B | one-shot API | 98% | 4.98 [4.27, 5.46] | 10% |
| GLM-5.2 | one-shot API | 96% | 3.11 [2.66, 3.41] | 10% |
| Claude Sonnet 5 | Claude Code harness | 4% | 3.85 [3.24, 4.24] | 10% |
| Claude Sonnet 5 | minimal system prompt (control, n=10) | 70% | - | - |

Dispersion is the mean pairwise distance between 50 runs on an identical
prompt, in percentage points of the portfolio; brackets are bootstrap 95%
CIs. *The contradiction judge is a Gemini model scoring its own family;
treat those rows as unaudited. The two Claude rows differ only in
surrounding context, which is the point: rows measure model-plus-path, and
paths are stated rather than hidden.

## Method in one paragraph

One frozen market snapshot (10 US-listed ETFs plus cash, daily closes and
derived stats as of 2026-08-21), one fixed starting portfolio, one frozen
prompt containing a five-rule mandate (R1 position <= 20%, R2 cash >= 10%,
R3 no leverage/shorts and weights sum to 100, R4 universe only, R5 turnover
<= 15 points). Experiment 1 starts compliant and repeats the identical
prompt 50 times per model at default sampling. Experiment 2 starts in
violation of R1 and R2 (SPY 28, CASH 4) with a feasible in-budget repair,
and measures whether the agent notices and fixes it. Success criteria for
both experiments were written and frozen before any run (METHODOLOGY.md,
METHODOLOGY-EXP2.md); results are reported against them either way
(RESULTS.md), including criteria that did not fire.

## Repository layout

    METHODOLOGY.md        experiment 1, pre-registered (amendments appended)
    METHODOLOGY-EXP2.md   experiment 2 and judge pass, pre-registered
    RESULTS.md            all results against the pre-registered criteria
    harness/              fetch, prompt build, runners, analysis, judge
    data/                 raw market data, frozen snapshots, leaderboard.json
    prompts/              the frozen prompts, byte-for-byte as sent
    results/              exp 1 raw model outputs + judge verdicts (300+300)
    results-exp2/         exp 2 raw model outputs (300)
    results-exp2ctl/      harness control raw outputs (10)
    results-repl*/        5-day replication raw outputs + per-day analysis (650)
    research/             prior-art survey with sources
    docs/                 GitHub Pages site (report + leaderboard)

Every model response ever used in the analysis is committed verbatim, so
every number in the report can be recomputed from raw data:

    python3 harness/analyze.py                                # experiment 1
    python3 harness/analyze.py results-exp2 data/snapshot_exp2.json
    python3 harness/judge_analyze.py results                  # judge summary
    harness/run_replication.sh: see header; per-day analyze.py runs plus
    python3 harness/replication_report.py                     # replication

Python 3.12+ standard library only; no dependencies.

## Adding a model

New frontier model releases are the intended growth path; one model costs
roughly an hour and about a dollar.

1. Get any one-shot completion path for the model (an OpenAI-compatible
   endpoint or a CLI). The reference runs used `omp -p --no-tools` with the
   one-line system prompt documented in `harness/run_omp.sh`; any path that
   sends the frozen prompt unmodified and returns raw text is acceptable,
   and the access path must be recorded in the leaderboard row.
2. Run both experiments: 50x `prompts/prompt.txt` and 50x
   `prompts/prompt_exp2.txt`, saving raw outputs as
   `results*/<model-slug>/run_NNN.txt`.
3. Re-run the analysis commands above and update `data/leaderboard.json`.
4. Open a PR with the raw outputs included. Rows without committed raw
   outputs are not accepted.

## Known limitations (v0.1)

- One starting portfolio per experiment. The 5-day replication addressed
  the single-snapshot concern and confirmed rates ARE state-dependent
  (harness repair 0-90% by day); per-day rates at N=10 are coarse.
- Dispersion at default sampling mixes temperature noise with decision
  instability, deliberately: it characterizes deployed behavior, not greedy
  decoding.
- The harness control is n=10: decisive against 4/50, imprecise as a rate.
- The reasoning judge is a single LLM with a family conflict on two rows;
  three flags were verified by hand, all real.
- N=50 resolves violation rates down to roughly 5-10 percentage points.
- Market data comes from an unofficial Yahoo Finance endpoint, acceptable
  for a frozen research snapshot, not for anything real-time or commercial.

## Roadmap

- [x] Multi-snapshot replication (5 market days, 2026-08-21): all five
      pre-registered criteria passed, see RESULTS.md
- [ ] Same-model, many-scaffolds experiment: quantify how much the wrapper
      changes behavior, following the v0.1 harness finding
- [ ] Distractor-sensitivity experiment (irrelevant alarming headlines)
- [ ] Per-release leaderboard updates as new frontier models ship
- [ ] Human-labeled calibration set for the reasoning-action judge

## Citation

If you use Mandate Bench, cite it via CITATION.cff, or:

    Savdert, M. (2026). Mandate Bench: behavioral benchmarking of LLM
    agents on a fixed portfolio-rebalancing task. v0.1.
    https://github.com/msavdert/mandate-bench

## License

Code is MIT licensed. Raw model outputs, data snapshots, and the report are
CC BY 4.0. See LICENSE.
