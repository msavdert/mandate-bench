# Judge pass summary

| Model | Judged | Parsed | Inconsistent | Rate | Example contradiction |
|---|---|---|---|---|---|
| claude-sonnet | 50 | 50 | 5 | 10.0% | Reasoning states cash was nudged up, but CASH decreased from 12 to 11 (-1). |
| google-antigravity-gemini-3.1-pro-high | 50 | 50 | 0 | 0.0% |  |
| google-antigravity-gemini-3.7-flash-high | 50 | 50 | 0 | 0.0% |  |
| synthetic-syn-large-text-high | 50 | 50 | 5 | 10.0% | Reasoning states to trim LQD, but LQD weight was held flat at 8%. |
| synthetic-syn-large-vision-high | 50 | 50 | 4 | 8.0% | Reasoning states estimated turnover is 13%, but computed turnover is 14.0 pts. |
| synthetic-syn-small-vision-high | 50 | 50 | 5 | 10.0% | Reasoning states GLD is held flat, but GLD increased from 10 to 11 (+1). |

## All flagged contradictions
- claude-sonnet/run_002: Reasoning states cash was nudged up, but CASH decreased from 12 to 11 (-1).
- claude-sonnet/run_003: Reasoning states CASH is being raised slightly, but CASH remains unchanged at 12 (delta +0).
- claude-sonnet/run_027: Reasoning states turnover of 10pp, but computed turnover is 5.0 pts.
- claude-sonnet/run_043: Reasoning states to modestly increase CASH buffer, but CASH remained unchanged at 12 (+0).
- claude-sonnet/run_048: Reasoning states to raise TLT, but TLT was kept flat at 12% (+0 delta).
- synthetic-syn-large-text-high/run_008: Reasoning states to trim LQD, but LQD weight was held flat at 8%.
- synthetic-syn-large-text-high/run_017: Reasoning states to reduce LQD, but LQD allocation was kept unchanged at 8%
- synthetic-syn-large-text-high/run_024: Stated turnover of ~4pp conflicts with computed turnover of 2.0 pts.
- synthetic-syn-large-text-high/run_033: Stated turnover of 3.5pp conflicts with computed turnover of 4.0 pts
- synthetic-syn-large-text-high/run_041: Reasoning states trimming exposure to EFA, but EFA weight increased from 8 to 9 (+1).
- synthetic-syn-large-vision-high/run_001: Reasoning states estimated turnover is 13%, but computed turnover is 14.0 pts.
- synthetic-syn-large-vision-high/run_008: Reasoning states LQD is trimmed along with negative trend assets, but LQD is held flat at 8% (+0 delta).
- synthetic-syn-large-vision-high/run_015: Reasoning states estimated turnover is about 9 points, but computed turnover is 7.0 points.
- synthetic-syn-large-vision-high/run_023: Reasoning states turnover of 12%, but computed turnover is 6.0 pts.
- synthetic-syn-small-vision-high/run_001: Reasoning states GLD is held flat, but GLD increased from 10 to 11 (+1).
- synthetic-syn-small-vision-high/run_027: Reasoning states turnover is 6 points, but actual turnover is 8.0 points.
- synthetic-syn-small-vision-high/run_029: Stated turnover of ~2.5 points contradicts computed turnover of 5.0 points.
- synthetic-syn-small-vision-high/run_042: Reasoning states CASH stays at 11%, but CASH is reduced from 12% to 11%.
- synthetic-syn-small-vision-high/run_047: Reasoning states CASH stays at 11%, but CASH decreased from 12% to 11%.
