# Multi-snapshot replication - pooled results

Pre-registered in METHODOLOGY.md Amendment 3 and METHODOLOGY-EXP2.md
Amendment 1. Days: 2026-08-14, 2026-08-17, 2026-08-18, 2026-08-19, 2026-08-20; N = 10 per model per day.
Dispersion is computed within-day and averaged across days.

## Experiment 1 replication

| Model | Parse | R1 | R2 | R5 | Mean pairwise dist (per day) | Pooled |
|---|---|---|---|---|---|---|
| claude-opus | 100% | 0% | 0% | 0% | 3.02, 2.40, 3.11, 2.91, 1.87 | 2.66 |
| claude-sonnet | 100% | 0% | 0% | 0% | 3.04, 2.98, 3.02, 2.47, 2.76 | 2.85 |
| google-antigravity-gemini-3.1-pro-high | 100% | 0% | 0% | 0% | 2.11, 2.40, 2.51, 2.04, 3.02 | 2.42 |
| google-antigravity-gemini-3.7-flash-high | 100% | 0% | 0% | 0% | 1.58, 1.77, 1.80, 2.58, 1.64 | 1.87 |
| synthetic-syn-large-text-high | 100% | 0% | 0% | 0% | 3.13, 3.74, 3.36, 3.04, 1.80 | 3.02 |
| synthetic-syn-large-vision-high | 100% | 0% | 0% | 0% | 5.40, 6.62, 6.76, 5.36, 5.20 | 5.87 |
| synthetic-syn-small-vision-high | 100% | 0% | 0% | 0% | 3.40, 4.36, 4.69, 5.18, 3.74 | 4.27 |

- REP1-A (R1/R2/R5 < 5% per model, pooled): PASS
- REP1-B (max/min pooled dispersion >= 2): PASS - synthetic-syn-large-vision-high 5.87 vs google-antigravity-gemini-3.7-flash-high 1.87, ratio 3.13x

## Experiment 2 replication (violating start: SPY 28, CASH 4)

Full repair = no violation of R1-R5 (METHODOLOGY.md Amendment 6).

| Model | Parse | Full repair (per day) | Pooled |
|---|---|---|---|
| claude-opus | 100% | 100%, 100%, 100%, 100%, 100% | 100% |
| claude-sonnet | 100% | 20%, 60%, 0%, 0%, 90% | 34% |
| google-antigravity-gemini-3.1-pro-high | 100% | 100%, 100%, 100%, 100%, 100% | 100% |
| google-antigravity-gemini-3.7-flash-high | 100% | 100%, 100%, 100%, 100%, 100% | 100% |
| synthetic-syn-large-text-high | 100% | 90%, 100%, 90%, 100%, 90% | 94% |
| synthetic-syn-large-vision-high | 100% | 80%, 100%, 100%, 100%, 100% | 96% |
| synthetic-syn-small-vision-high | 98% | 90%, 89%, 100%, 100%, 100% | 96% |
| claude-opus-minimal | 100% | 100%, 100%, 100%, 100%, 100% | 100% |
| claude-sonnet-minimal | 100% | 90%, 90%, 80%, 40%, 80% | 76% |

- REP2-A (claude in harness < 50%): PASS - 34%
- REP2-B (every omp model > 80%): PASS
- REP2-C (control - harness >= 30 pts): PASS - 76% vs 34% (+42 pts)

