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
| QQQ | 14.70 | 0.67 | 80.0% | hold |
| IWM | 5.90 | 0.99 | 50.0% | increase |
| EFA | 8.80 | 0.92 | 50.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.20 | 0.63 | 90.0% | hold |
| LQD | 6.20 | 0.63 | 90.0% | hold |
| GLD | 11.60 | 0.97 | 60.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.60 | 1.07 | 100.0% | increase |

Mean pairwise distance: 2.76 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.76 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 90.0% |
| R2 | CASH < 10% | 100.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 26.80 | 2.57 | 70.0% | hold |
| QQQ | 14.90 | 0.32 | 90.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.50 | 0.85 | 70.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 10.50 | 1.51 | 80.0% | decrease |
| DBC | 2.90 | 0.32 | 90.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 6.40 | 1.26 | 90.0% | increase |

Mean pairwise distance: 3.22 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=100.0% -> MET
- S2 (mean pairwise distance >= 10 points): 3.22 -> not met
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
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.20 | 0.63 | 90.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 13.00 | 1.05 | 50.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.80 | 1.03 | 100.0% | increase |

Mean pairwise distance: 1.29 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.29 -> not met
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
| TLT | 10.00 | 0.00 | 100.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 13.20 | 1.03 | 60.0% | increase |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.80 | 1.03 | 100.0% | increase |

Mean pairwise distance: 1.07 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.07 -> not met
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
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 14.50 | 1.08 | 80.0% | hold |
| IWM | 5.30 | 0.95 | 90.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.20 | 1.14 | 70.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 12.90 | 0.99 | 50.0% | increase |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.10 | 1.52 | 100.0% | increase |

Mean pairwise distance: 2.67 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.67 -> not met
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
| SPY | 19.80 | 0.63 | 100.0% | decrease |
| QQQ | 13.80 | 1.55 | 60.0% | hold |
| IWM | 5.60 | 1.58 | 80.0% | hold |
| EFA | 8.40 | 0.84 | 80.0% | hold |
| EEM | 3.60 | 0.70 | 70.0% | hold |
| TLT | 10.00 | 2.67 | 50.0% | hold |
| LQD | 6.40 | 0.84 | 80.0% | hold |
| GLD | 13.40 | 1.58 | 50.0% | increase |
| DBC | 3.40 | 0.70 | 70.0% | hold |
| VNQ | 4.90 | 0.32 | 90.0% | hold |
| CASH | 10.70 | 0.95 | 100.0% | increase |

Mean pairwise distance: 5.87 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 5.87 -> not met
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
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 14.30 | 0.82 | 50.0% | decrease |
| IWM | 5.80 | 0.92 | 50.0% | increase |
| EFA | 8.10 | 0.32 | 90.0% | hold |
| EEM | 3.80 | 0.42 | 80.0% | hold |
| TLT | 10.20 | 1.23 | 50.0% | hold |
| LQD | 5.90 | 0.32 | 90.0% | hold |
| GLD | 12.10 | 1.20 | 60.0% | hold |
| DBC | 3.20 | 0.63 | 90.0% | hold |
| VNQ | 5.30 | 0.48 | 70.0% | hold |
| CASH | 11.30 | 1.49 | 100.0% | increase |

Mean pairwise distance: 3.93 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.93 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=5.50 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

