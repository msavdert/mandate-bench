# Mandate Bench - Results Summary

See METHODOLOGY.md for metric definitions and pre-registered
success criteria (S1/S2/S3, null-result criteria).

## claude-sonnet

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
| SPY | 17.78 | 0.51 | 76.0% | hold |
| QQQ | 13.42 | 0.88 | 86.0% | decrease |
| IWM | 5.02 | 0.14 | 98.0% | hold |
| EFA | 8.32 | 0.51 | 70.0% | hold |
| EEM | 4.06 | 0.31 | 90.0% | hold |
| TLT | 10.78 | 1.11 | 62.0% | decrease |
| LQD | 8.00 | 0.20 | 96.0% | hold |
| GLD | 11.50 | 1.98 | 72.0% | increase |
| DBC | 3.22 | 0.46 | 80.0% | hold |
| VNQ | 4.92 | 0.27 | 92.0% | hold |
| CASH | 12.98 | 1.73 | 48.0% | hold |

Mean pairwise distance: 3.85 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.85 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

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
| SPY | 17.74 | 0.69 | 86.0% | hold |
| QQQ | 12.88 | 1.33 | 80.0% | decrease |
| IWM | 5.04 | 0.28 | 98.0% | hold |
| EFA | 8.04 | 0.28 | 98.0% | hold |
| EEM | 3.96 | 0.35 | 94.0% | hold |
| TLT | 9.64 | 1.35 | 86.0% | decrease |
| LQD | 7.52 | 1.07 | 82.0% | hold |
| GLD | 14.24 | 1.46 | 100.0% | increase |
| DBC | 3.82 | 1.00 | 56.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.12 | 0.52 | 94.0% | hold |

Mean pairwise distance: 3.65 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.65 -> not met
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
| SPY | 17.98 | 0.14 | 98.0% | hold |
| QQQ | 12.80 | 0.88 | 94.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.84 | 0.96 | 54.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 8.90 | 0.51 | 100.0% | decrease |
| LQD | 7.10 | 0.91 | 54.0% | decrease |
| GLD | 13.80 | 0.45 | 100.0% | increase |
| DBC | 4.94 | 0.42 | 96.0% | increase |
| VNQ | 4.78 | 0.55 | 84.0% | hold |
| CASH | 11.86 | 0.50 | 92.0% | hold |

Mean pairwise distance: 2.31 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.31 -> not met
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
| SPY | 18.14 | 0.40 | 88.0% | hold |
| QQQ | 13.76 | 0.96 | 70.0% | decrease |
| IWM | 5.64 | 0.75 | 52.0% | hold |
| EFA | 8.44 | 0.58 | 60.0% | hold |
| EEM | 4.06 | 0.37 | 92.0% | hold |
| TLT | 10.22 | 0.76 | 92.0% | decrease |
| LQD | 7.54 | 0.71 | 66.0% | hold |
| GLD | 11.84 | 1.11 | 90.0% | increase |
| DBC | 3.24 | 0.48 | 78.0% | hold |
| VNQ | 5.02 | 0.14 | 98.0% | hold |
| CASH | 12.20 | 0.53 | 80.0% | hold |

Mean pairwise distance: 3.11 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.11 -> not met
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
| SPY | 18.32 | 0.87 | 70.0% | hold |
| QQQ | 12.76 | 1.66 | 78.0% | decrease |
| IWM | 5.34 | 0.75 | 80.0% | hold |
| EFA | 9.36 | 1.31 | 66.0% | increase |
| EEM | 4.08 | 0.88 | 68.0% | hold |
| TLT | 9.06 | 1.27 | 96.0% | decrease |
| LQD | 6.36 | 0.96 | 86.0% | decrease |
| GLD | 14.34 | 1.86 | 98.0% | increase |
| DBC | 4.38 | 1.03 | 72.0% | increase |
| VNQ | 4.68 | 0.59 | 74.0% | hold |
| CASH | 11.32 | 1.10 | 46.0% | decrease |

Mean pairwise distance: 6.27 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 6.27 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

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
| SPY | 18.04 | 0.28 | 92.0% | hold |
| QQQ | 13.26 | 0.88 | 90.0% | decrease |
| IWM | 5.62 | 0.70 | 50.0% | increase |
| EFA | 9.66 | 0.80 | 94.0% | increase |
| EEM | 4.02 | 0.32 | 90.0% | hold |
| TLT | 9.82 | 1.02 | 94.0% | decrease |
| LQD | 7.32 | 0.91 | 54.0% | decrease |
| GLD | 11.82 | 1.95 | 70.0% | increase |
| DBC | 3.70 | 0.74 | 54.0% | increase |
| VNQ | 4.56 | 0.61 | 62.0% | hold |
| CASH | 12.20 | 1.36 | 44.0% | hold |

Mean pairwise distance: 4.98 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.98 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=2.71 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

