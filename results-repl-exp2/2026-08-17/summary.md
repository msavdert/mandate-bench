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
| R1 | any non-CASH instrument > 20% | 40.0% |
| R2 | CASH < 10% | 40.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 22.70 | 3.50 | 100.0% | decrease |
| QQQ | 15.20 | 0.63 | 90.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.60 | 0.70 | 50.0% | hold |
| TLT | 8.30 | 1.06 | 80.0% | decrease |
| LQD | 5.70 | 0.48 | 70.0% | hold |
| GLD | 13.80 | 1.23 | 80.0% | increase |
| DBC | 3.70 | 0.67 | 60.0% | increase |
| VNQ | 4.70 | 0.48 | 70.0% | hold |
| CASH | 8.30 | 3.16 | 80.0% | increase |

Mean pairwise distance: 6.33 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=40.0% -> MET
- S2 (mean pairwise distance >= 10 points): 6.33 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

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
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.60 | 1.35 | 80.0% | hold |
| TLT | 9.80 | 0.63 | 90.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 12.60 | 0.97 | 70.0% | hold |
| DBC | 3.20 | 0.63 | 90.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.80 | 1.03 | 100.0% | increase |

Mean pairwise distance: 1.96 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.96 -> not met
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
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.80 | 0.92 | 50.0% | hold |
| TLT | 8.80 | 1.32 | 50.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 13.30 | 0.82 | 80.0% | increase |
| DBC | 3.30 | 0.67 | 80.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.80 | 0.92 | 100.0% | increase |

Mean pairwise distance: 2.49 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.49 -> not met
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
| SPY | 19.80 | 0.63 | 100.0% | decrease |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 6.10 | 0.32 | 100.0% | increase |
| TLT | 9.40 | 0.97 | 70.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 12.10 | 0.32 | 90.0% | hold |
| DBC | 3.20 | 0.42 | 80.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.40 | 0.84 | 100.0% | increase |

Mean pairwise distance: 1.40 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.40 -> not met
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
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 15.30 | 0.67 | 80.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 5.70 | 1.95 | 60.0% | increase |
| TLT | 8.00 | 2.26 | 50.0% | hold |
| LQD | 5.50 | 0.71 | 60.0% | hold |
| GLD | 12.70 | 0.95 | 60.0% | hold |
| DBC | 3.60 | 1.07 | 70.0% | hold |
| VNQ | 4.80 | 0.63 | 90.0% | hold |
| CASH | 11.40 | 0.97 | 100.0% | increase |

Mean pairwise distance: 4.67 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.67 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## synthetic-syn-small-vision-high

Total run files found: 10
Usable (parsed) runs: 9
Parse rate: 90.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 0.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 11.1% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 15.11 | 0.78 | 77.8% | hold |
| IWM | 5.11 | 0.33 | 88.9% | hold |
| EFA | 8.44 | 0.73 | 66.7% | hold |
| EEM | 5.33 | 0.87 | 77.8% | increase |
| TLT | 8.56 | 1.13 | 66.7% | decrease |
| LQD | 5.56 | 0.73 | 66.7% | hold |
| GLD | 12.11 | 0.78 | 77.8% | hold |
| DBC | 3.67 | 0.87 | 55.6% | hold |
| VNQ | 4.67 | 0.71 | 77.8% | hold |
| CASH | 11.67 | 1.22 | 100.0% | increase |

Mean pairwise distance: 4.03 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.03 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=4.52 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

