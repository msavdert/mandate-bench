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
| SPY | 18.10 | 0.88 | 40.0% | increase |
| QQQ | 13.00 | 0.00 | 100.0% | decrease |
| IWM | 6.20 | 0.63 | 90.0% | increase |
| EFA | 8.90 | 0.57 | 80.0% | increase |
| EEM | 2.30 | 0.48 | 100.0% | decrease |
| TLT | 11.40 | 0.70 | 50.0% | hold |
| LQD | 8.80 | 0.63 | 70.0% | increase |
| GLD | 9.10 | 0.32 | 90.0% | decrease |
| DBC | 3.30 | 0.48 | 70.0% | hold |
| VNQ | 5.20 | 0.42 | 80.0% | hold |
| CASH | 13.70 | 0.95 | 90.0% | increase |

Mean pairwise distance: 3.11 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.11 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

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
| QQQ | 13.60 | 0.97 | 70.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 3.00 | 0.82 | 70.0% | decrease |
| TLT | 12.50 | 0.71 | 60.0% | hold |
| LQD | 8.00 | 0.00 | 100.0% | hold |
| GLD | 9.40 | 0.84 | 60.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.10 | 0.32 | 90.0% | hold |
| CASH | 14.40 | 2.01 | 70.0% | increase |

Mean pairwise distance: 3.02 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.02 -> not met
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
| SPY | 18.20 | 0.79 | 70.0% | hold |
| QQQ | 14.00 | 0.82 | 70.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 3.10 | 0.74 | 70.0% | decrease |
| TLT | 12.60 | 0.70 | 50.0% | increase |
| LQD | 8.00 | 0.00 | 100.0% | hold |
| GLD | 10.00 | 0.00 | 100.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 13.10 | 1.52 | 70.0% | increase |

Mean pairwise distance: 2.51 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.51 -> not met
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
| SPY | 18.00 | 0.00 | 100.0% | hold |
| QQQ | 13.00 | 0.00 | 100.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 2.60 | 0.52 | 100.0% | decrease |
| TLT | 12.70 | 0.67 | 60.0% | increase |
| LQD | 8.20 | 0.42 | 80.0% | hold |
| GLD | 10.00 | 0.00 | 100.0% | hold |
| DBC | 4.20 | 0.79 | 80.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 13.30 | 0.95 | 80.0% | increase |

Mean pairwise distance: 1.80 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.80 -> not met
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
| SPY | 18.40 | 0.84 | 50.0% | hold |
| QQQ | 13.50 | 0.85 | 80.0% | decrease |
| IWM | 6.10 | 0.99 | 60.0% | increase |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 2.50 | 0.71 | 90.0% | decrease |
| TLT | 11.40 | 0.97 | 70.0% | hold |
| LQD | 7.80 | 0.63 | 90.0% | hold |
| GLD | 10.10 | 0.32 | 90.0% | hold |
| DBC | 3.10 | 0.32 | 90.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 13.90 | 1.20 | 90.0% | increase |

Mean pairwise distance: 3.36 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.36 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

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
| SPY | 18.80 | 0.92 | 50.0% | hold |
| QQQ | 14.00 | 1.70 | 50.0% | hold |
| IWM | 5.60 | 1.35 | 80.0% | hold |
| EFA | 9.10 | 1.85 | 50.0% | hold |
| EEM | 3.00 | 0.94 | 60.0% | decrease |
| TLT | 10.00 | 1.41 | 80.0% | decrease |
| LQD | 7.60 | 0.84 | 50.0% | hold |
| GLD | 10.10 | 1.60 | 60.0% | hold |
| DBC | 3.80 | 0.79 | 60.0% | increase |
| VNQ | 4.90 | 0.32 | 90.0% | hold |
| CASH | 13.10 | 1.29 | 60.0% | increase |

Mean pairwise distance: 6.76 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 6.76 -> not met
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
| SPY | 18.40 | 0.52 | 60.0% | hold |
| QQQ | 14.30 | 0.67 | 60.0% | decrease |
| IWM | 5.60 | 0.84 | 60.0% | hold |
| EFA | 9.40 | 0.84 | 90.0% | increase |
| EEM | 2.70 | 0.67 | 90.0% | decrease |
| TLT | 10.50 | 1.27 | 90.0% | decrease |
| LQD | 8.40 | 0.84 | 50.0% | hold |
| GLD | 9.60 | 0.97 | 60.0% | hold |
| DBC | 3.40 | 0.52 | 60.0% | hold |
| VNQ | 4.80 | 0.42 | 80.0% | hold |
| CASH | 12.90 | 1.52 | 70.0% | increase |

Mean pairwise distance: 4.69 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.69 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=3.75 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

