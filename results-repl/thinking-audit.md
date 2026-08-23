<!-- Regenerate with: python3 harness/thinking_audit.py > results-repl/thinking-audit.md -->

# Extended-thinking mediation audit

Reproduces the thinking-mediation finding directly from committed run
artifacts under results-exp2/, results-exp2ctl/, results-repl-exp2/, and
results-repl-exp2ctl/. No model is re-run. Repair = R1+R2 clear only
(harness/replication_report.py:48), not all-rules (R1-R5) compliance.

## Per-arm, per-day

| Arm | Date | n | Thinking-on | Repaired |
|---|---|---|---|---|
| Sonnet harness | 2026-08-21 | 50 | 6% (3/50) | 4% (2/50) |
| Sonnet harness | 2026-08-14 | 10 | 30% (3/10) | 20% (2/10) |
| Sonnet harness | 2026-08-17 | 10 | 60% (6/10) | 60% (6/10) |
| Sonnet harness | 2026-08-18 | 10 | 10% (1/10) | 0% (0/10) |
| Sonnet harness | 2026-08-19 | 10 | 20% (2/10) | 0% (0/10) |
| Sonnet harness | 2026-08-20 | 10 | 100% (10/10) | 90% (9/10) |
| Sonnet minimal control | 2026-08-21 | 10 | 100% (10/10) | 70% (7/10) |
| Sonnet minimal control | 2026-08-14 | 10 | 100% (10/10) | 90% (9/10) |
| Sonnet minimal control | 2026-08-17 | 10 | 100% (10/10) | 90% (9/10) |
| Sonnet minimal control | 2026-08-18 | 10 | 100% (10/10) | 80% (8/10) |
| Sonnet minimal control | 2026-08-19 | 10 | 100% (10/10) | 40% (4/10) |
| Sonnet minimal control | 2026-08-20 | 10 | 100% (10/10) | 80% (8/10) |
| Opus harness | 2026-08-21 | 10 | 100% (10/10) | 100% (10/10) |
| Opus harness | 2026-08-14 | 10 | 100% (10/10) | 100% (10/10) |
| Opus harness | 2026-08-17 | 10 | 100% (10/10) | 100% (10/10) |
| Opus harness | 2026-08-18 | 10 | 100% (10/10) | 100% (10/10) |
| Opus harness | 2026-08-19 | 10 | 100% (10/10) | 100% (10/10) |
| Opus harness | 2026-08-20 | 10 | 100% (10/10) | 100% (10/10) |
| Opus minimal control | 2026-08-21 | 10 | 100% (10/10) | 100% (10/10) |
| Opus minimal control | 2026-08-14 | 10 | 100% (10/10) | 100% (10/10) |
| Opus minimal control | 2026-08-17 | 10 | 100% (10/10) | 100% (10/10) |
| Opus minimal control | 2026-08-18 | 10 | 100% (10/10) | 100% (10/10) |
| Opus minimal control | 2026-08-19 | 10 | 100% (10/10) | 100% (10/10) |
| Opus minimal control | 2026-08-20 | 10 | 100% (10/10) | 100% (10/10) |

## Pooled 2x2 cross-tabs (thinking off/on x repair no/yes)

| Arm | Thinking off, no repair | Thinking off, repaired | Thinking on, no repair | Thinking on, repaired |
|---|---|---|---|---|
| Sonnet harness | 75/75 | 0/75 | 6/25 | 19/25 |
| Sonnet minimal control | 0/0 | 0/0 | 15/60 | 45/60 |
| Opus harness | 0/0 | 0/0 | 0/60 | 60/60 |
| Opus minimal control | 0/0 | 0/0 | 0/60 | 60/60 |

## Day-level paired statistics (control minus harness repair %)

| Date | Harness repair % | Control repair % | Diff (pts) |
|---|---|---|---|
| 2026-08-21 | 4% | 70% | +66 |
| 2026-08-14 | 20% | 90% | +70 |
| 2026-08-17 | 60% | 90% | +30 |
| 2026-08-18 | 0% | 80% | +80 |
| 2026-08-19 | 0% | 40% | +40 |
| 2026-08-20 | 90% | 80% | -10 |

- Five replication days (08-14..08-20): mean +42.0 pts, sd 35.6, t(4) = 2.64, p = 0.058
- All six days (adds 08-21): mean +46.0 pts, sd 33.3, t(5) = 3.38, p = 0.020

- Opus harness minus Sonnet harness, paired over six days: mean +71.0 pts, sd 37.6, t(5) = 4.62, p = 0.006

## Mean total input tokens per arm per day

input_tokens + cache_creation_input_tokens + cache_read_input_tokens.

| Arm | 2026-08-21 | 2026-08-14 | 2026-08-17 | 2026-08-18 | 2026-08-19 | 2026-08-20 |
|---|---|---|---|---|---|---|
| Sonnet harness | 11812 | 12035 | 12060 | 12084 | 12090 | 12118 |
| Sonnet minimal control | 3300 | 3301 | 3302 | 3308 | 3296 | 3306 |
| Opus harness | 7164 | 6746 | 6834 | 6927 | 7002 | 7099 |
| Opus minimal control | 3284 | 3285 | 3286 | 3292 | 3280 | 3290 |

