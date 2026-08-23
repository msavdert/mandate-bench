# Mandate Bench - Results Summary

See METHODOLOGY.md for metric definitions and pre-registered
success criteria (S1/S2/S3, null-result criteria).

## claude-opus

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 0.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 14.90 | 0.32 | 90.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 10.10 | 0.32 | 100.0% | increase |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.00 | 0.00 | 100.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 11.90 | 0.32 | 90.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.10 | 0.32 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 0.40 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 0.40 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet

Total run files found: 50
Usable (parsed) runs: 50
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 96.0% |
| R2 | CASH < 10% | 90.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 27.36 | 1.71 | 78.0% | hold |
| QQQ | 13.96 | 0.92 | 62.0% | decrease |
| IWM | 5.10 | 0.36 | 86.0% | hold |
| EFA | 8.22 | 0.55 | 84.0% | hold |
| EEM | 4.06 | 0.31 | 90.0% | hold |
| TLT | 9.62 | 0.83 | 72.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 10.78 | 1.45 | 74.0% | decrease |
| DBC | 2.96 | 0.20 | 96.0% | hold |
| VNQ | 4.98 | 0.14 | 98.0% | hold |
| CASH | 6.96 | 1.75 | 96.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 2/50 (4.0%)

Mean pairwise distance: 3.56 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=96.0% -> MET
- S2 (mean pairwise distance >= 10 points): 3.56 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## google-antigravity-gemini-3.1-pro-high

Total run files found: 50
Usable (parsed) runs: 50
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 0.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.08 | 0.40 | 96.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 13.04 | 1.01 | 52.0% | increase |
| DBC | 3.04 | 0.28 | 98.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.84 | 1.00 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 50/50 (100.0%)

Mean pairwise distance: 1.12 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.12 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## google-antigravity-gemini-3.7-flash-high

Total run files found: 50
Usable (parsed) runs: 50
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 0.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 19.98 | 0.14 | 100.0% | decrease |
| QQQ | 14.90 | 0.30 | 90.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.08 | 0.34 | 94.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.24 | 1.04 | 64.0% | hold |
| LQD | 5.92 | 0.40 | 96.0% | hold |
| GLD | 14.46 | 0.73 | 100.0% | increase |
| DBC | 3.26 | 0.60 | 82.0% | hold |
| VNQ | 4.96 | 0.20 | 96.0% | hold |
| CASH | 10.20 | 0.53 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 50/50 (100.0%)

Mean pairwise distance: 1.57 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.57 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## synthetic-syn-large-text-high

Total run files found: 50
Usable (parsed) runs: 50
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 0.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 4.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 19.92 | 0.34 | 100.0% | decrease |
| QQQ | 14.76 | 0.62 | 86.0% | hold |
| IWM | 5.18 | 0.52 | 88.0% | hold |
| EFA | 8.28 | 0.61 | 80.0% | hold |
| EEM | 4.04 | 0.28 | 98.0% | hold |
| TLT | 9.56 | 0.84 | 78.0% | hold |
| LQD | 5.98 | 0.14 | 98.0% | hold |
| GLD | 13.20 | 1.12 | 64.0% | increase |
| DBC | 3.14 | 0.50 | 92.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.92 | 1.40 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 48/50 (96.0%)

Mean pairwise distance: 2.50 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.50 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## synthetic-syn-large-vision-high

Total run files found: 50
Usable (parsed) runs: 50
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 0.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 19.96 | 0.28 | 100.0% | decrease |
| QQQ | 14.04 | 1.50 | 66.0% | hold |
| IWM | 5.04 | 0.20 | 96.0% | hold |
| EFA | 8.62 | 1.05 | 68.0% | hold |
| EEM | 4.00 | 0.20 | 96.0% | hold |
| TLT | 9.42 | 1.01 | 72.0% | hold |
| LQD | 5.74 | 0.60 | 82.0% | hold |
| GLD | 14.18 | 1.91 | 74.0% | increase |
| DBC | 3.38 | 0.70 | 74.0% | hold |
| VNQ | 4.86 | 0.53 | 88.0% | hold |
| CASH | 10.76 | 1.36 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 50/50 (100.0%)

Mean pairwise distance: 4.08 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.08 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## synthetic-syn-small-vision-high

Total run files found: 50
Usable (parsed) runs: 50
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 0.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 2.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 19.96 | 0.20 | 100.0% | decrease |
| QQQ | 14.20 | 1.01 | 56.0% | hold |
| IWM | 5.46 | 0.65 | 60.0% | hold |
| EFA | 9.30 | 1.05 | 74.0% | increase |
| EEM | 4.08 | 0.34 | 88.0% | hold |
| TLT | 8.90 | 0.99 | 58.0% | decrease |
| LQD | 5.62 | 0.49 | 62.0% | hold |
| GLD | 12.64 | 1.31 | 48.0% | hold |
| DBC | 3.44 | 0.58 | 60.0% | hold |
| VNQ | 4.86 | 0.53 | 76.0% | hold |
| CASH | 11.52 | 1.69 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 49/50 (98.0%)

Mean pairwise distance: 4.43 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.43 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=11.08 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

