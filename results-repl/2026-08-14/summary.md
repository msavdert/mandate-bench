# Mandate Bench - Results Summary

See METHODOLOGY.md for metric definitions and pre-registered
success criteria (S1/S2/S3, null-result criteria).

## claude-sonnet

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
| SPY | 18.00 | 0.00 | 100.0% | hold |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.20 | 0.42 | 80.0% | hold |
| EFA | 8.10 | 0.32 | 90.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.70 | 0.67 | 100.0% | decrease |
| LQD | 7.40 | 0.84 | 60.0% | hold |
| GLD | 11.70 | 1.25 | 80.0% | increase |
| DBC | 4.10 | 0.99 | 60.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.80 | 1.32 | 40.0% | decrease |

Mean pairwise distance: 3.04 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.04 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## google-antigravity-gemini-3.1-pro-high

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
| SPY | 18.10 | 0.32 | 90.0% | hold |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.40 | 0.70 | 70.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.70 | 0.67 | 100.0% | decrease |
| LQD | 7.20 | 0.92 | 50.0% | decrease |
| GLD | 11.80 | 0.79 | 90.0% | increase |
| DBC | 3.80 | 0.92 | 50.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.00 | 0.00 | 100.0% | hold |

Mean pairwise distance: 2.11 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.11 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## google-antigravity-gemini-3.7-flash-high

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
| SPY | 17.90 | 0.32 | 90.0% | hold |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 6.60 | 0.70 | 90.0% | increase |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.30 | 0.48 | 100.0% | decrease |
| LQD | 6.20 | 0.42 | 100.0% | decrease |
| GLD | 11.50 | 0.71 | 90.0% | increase |
| DBC | 4.50 | 0.71 | 90.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.00 | 0.00 | 100.0% | hold |

Mean pairwise distance: 1.58 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.58 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## synthetic-syn-large-text-high

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
| SPY | 18.10 | 0.32 | 90.0% | hold |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 6.40 | 0.84 | 80.0% | increase |
| EFA | 8.70 | 0.67 | 60.0% | increase |
| EEM | 3.60 | 0.52 | 60.0% | hold |
| TLT | 9.60 | 0.70 | 100.0% | decrease |
| LQD | 7.10 | 0.74 | 70.0% | decrease |
| GLD | 10.30 | 0.48 | 70.0% | hold |
| DBC | 3.40 | 0.70 | 70.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.80 | 1.14 | 60.0% | increase |

Mean pairwise distance: 3.13 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.13 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## synthetic-syn-large-vision-high

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
| SPY | 18.70 | 0.95 | 60.0% | hold |
| QQQ | 15.10 | 0.32 | 90.0% | hold |
| IWM | 6.40 | 1.07 | 70.0% | increase |
| EFA | 9.10 | 0.88 | 70.0% | increase |
| EEM | 3.70 | 0.67 | 80.0% | hold |
| TLT | 8.00 | 1.25 | 100.0% | decrease |
| LQD | 6.10 | 0.74 | 100.0% | decrease |
| GLD | 12.00 | 1.94 | 60.0% | increase |
| DBC | 4.40 | 0.97 | 80.0% | increase |
| VNQ | 4.80 | 0.42 | 80.0% | hold |
| CASH | 11.70 | 0.95 | 70.0% | hold |

Mean pairwise distance: 5.40 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 5.40 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## synthetic-syn-small-vision-high

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
| SPY | 18.30 | 0.48 | 70.0% | hold |
| QQQ | 14.70 | 0.67 | 80.0% | hold |
| IWM | 6.70 | 0.48 | 100.0% | increase |
| EFA | 9.00 | 0.67 | 80.0% | increase |
| EEM | 3.60 | 0.52 | 60.0% | hold |
| TLT | 9.80 | 0.79 | 100.0% | decrease |
| LQD | 6.80 | 0.79 | 80.0% | decrease |
| GLD | 10.40 | 0.70 | 70.0% | hold |
| DBC | 3.60 | 0.52 | 60.0% | increase |
| VNQ | 5.00 | 0.47 | 80.0% | hold |
| CASH | 12.10 | 0.74 | 50.0% | hold |

Mean pairwise distance: 3.40 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.40 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=3.42 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

