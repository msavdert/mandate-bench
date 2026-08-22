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
| R1 | any non-CASH instrument > 20% | 80.0% |
| R2 | CASH < 10% | 60.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 25.80 | 3.22 | 50.0% | decrease |
| QQQ | 14.70 | 0.67 | 80.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 7.90 | 0.32 | 90.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.00 | 0.94 | 60.0% | decrease |
| LQD | 5.60 | 0.52 | 60.0% | hold |
| GLD | 12.70 | 0.95 | 60.0% | hold |
| DBC | 3.20 | 0.42 | 80.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 7.10 | 3.84 | 50.0% | increase |

Mean pairwise distance: 5.60 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=80.0% -> MET
- S2 (mean pairwise distance >= 10 points): 5.60 -> not met
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
| IWM | 5.70 | 1.64 | 80.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.70 | 0.95 | 90.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 12.20 | 0.63 | 90.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.40 | 0.97 | 100.0% | increase |

Mean pairwise distance: 1.62 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.62 -> not met
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
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.60 | 0.84 | 80.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 12.40 | 0.84 | 80.0% | hold |
| DBC | 3.20 | 0.63 | 90.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.80 | 0.63 | 100.0% | increase |

Mean pairwise distance: 1.11 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.11 -> not met
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
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 10.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 19.90 | 0.32 | 100.0% | decrease |
| QQQ | 15.10 | 0.32 | 90.0% | hold |
| IWM | 6.30 | 1.06 | 70.0% | increase |
| EFA | 8.60 | 0.97 | 70.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 8.90 | 1.20 | 50.0% | hold |
| LQD | 5.70 | 0.67 | 80.0% | hold |
| GLD | 12.20 | 0.63 | 90.0% | hold |
| DBC | 3.30 | 0.67 | 80.0% | hold |
| VNQ | 5.20 | 0.63 | 90.0% | hold |
| CASH | 10.60 | 1.26 | 100.0% | increase |

Mean pairwise distance: 3.42 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.42 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## synthetic-syn-large-vision-high

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 10.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 10.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 20.20 | 0.63 | 100.0% | decrease |
| QQQ | 15.10 | 0.74 | 80.0% | hold |
| IWM | 6.00 | 1.41 | 60.0% | hold |
| EFA | 9.20 | 1.32 | 50.0% | increase |
| EEM | 3.70 | 0.95 | 90.0% | hold |
| TLT | 8.30 | 2.50 | 50.0% | decrease |
| LQD | 5.50 | 0.85 | 70.0% | hold |
| GLD | 12.50 | 2.01 | 40.0% | increase |
| DBC | 3.70 | 1.16 | 70.0% | hold |
| VNQ | 4.80 | 0.63 | 90.0% | hold |
| CASH | 11.20 | 1.93 | 100.0% | increase |

Mean pairwise distance: 7.00 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=10.0% -> MET
- S2 (mean pairwise distance >= 10 points): 7.00 -> not met
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
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 10.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 14.90 | 0.32 | 90.0% | hold |
| IWM | 6.50 | 0.97 | 80.0% | increase |
| EFA | 9.10 | 0.99 | 70.0% | increase |
| EEM | 3.70 | 0.48 | 70.0% | hold |
| TLT | 8.70 | 1.06 | 70.0% | decrease |
| LQD | 5.70 | 0.48 | 70.0% | hold |
| GLD | 12.00 | 0.94 | 80.0% | hold |
| DBC | 3.20 | 0.42 | 80.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.80 | 1.40 | 100.0% | increase |

Mean pairwise distance: 3.53 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.53 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=6.30 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

