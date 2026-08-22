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
| QQQ | 13.90 | 1.20 | 50.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 9.00 | 0.94 | 60.0% | increase |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.90 | 0.32 | 90.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 12.20 | 0.63 | 90.0% | hold |
| DBC | 4.60 | 0.70 | 90.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.40 | 0.84 | 100.0% | increase |

Mean pairwise distance: 2.18 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.18 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 10.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 20.50 | 1.58 | 100.0% | decrease |
| QQQ | 13.60 | 0.70 | 90.0% | decrease |
| IWM | 4.80 | 0.42 | 80.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.47 | 80.0% | hold |
| TLT | 9.10 | 0.74 | 70.0% | decrease |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 13.80 | 1.23 | 90.0% | increase |
| DBC | 3.90 | 0.88 | 60.0% | increase |
| VNQ | 4.80 | 0.42 | 80.0% | hold |
| CASH | 11.50 | 1.65 | 100.0% | increase |

Mean pairwise distance: 3.98 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=10.0% -> MET
- S2 (mean pairwise distance >= 10 points): 3.98 -> not met
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
| TLT | 10.00 | 0.00 | 100.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 13.00 | 1.05 | 50.0% | increase |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.00 | 1.05 | 100.0% | increase |

Mean pairwise distance: 1.11 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.11 -> not met
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
| TLT | 9.80 | 0.63 | 90.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 12.80 | 1.14 | 60.0% | hold |
| DBC | 4.00 | 0.94 | 60.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 10.40 | 0.84 | 100.0% | increase |

Mean pairwise distance: 1.69 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.69 -> not met
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
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 13.80 | 1.32 | 50.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.40 | 0.52 | 60.0% | hold |
| TLT | 9.60 | 0.84 | 80.0% | hold |
| LQD | 6.00 | 0.00 | 100.0% | hold |
| GLD | 13.40 | 0.97 | 70.0% | increase |
| DBC | 3.90 | 0.88 | 60.0% | increase |
| VNQ | 5.00 | 0.47 | 80.0% | hold |
| CASH | 10.80 | 1.03 | 100.0% | increase |

Mean pairwise distance: 3.06 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.06 -> not met
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
| SPY | 20.00 | 0.00 | 100.0% | decrease |
| QQQ | 13.30 | 1.70 | 60.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.20 | 0.63 | 90.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.40 | 0.84 | 60.0% | hold |
| LQD | 5.80 | 0.42 | 80.0% | hold |
| GLD | 13.60 | 1.51 | 60.0% | increase |
| DBC | 4.70 | 1.34 | 70.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.00 | 0.94 | 100.0% | increase |

Mean pairwise distance: 3.93 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.93 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

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
| SPY | 19.90 | 0.32 | 100.0% | decrease |
| QQQ | 13.90 | 1.20 | 60.0% | decrease |
| IWM | 5.40 | 0.70 | 70.0% | hold |
| EFA | 9.10 | 0.88 | 70.0% | increase |
| EEM | 4.10 | 0.32 | 90.0% | hold |
| TLT | 9.10 | 0.99 | 50.0% | hold |
| LQD | 6.10 | 0.32 | 90.0% | hold |
| GLD | 12.60 | 1.17 | 50.0% | hold |
| DBC | 3.60 | 0.84 | 60.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.20 | 1.62 | 100.0% | increase |

Mean pairwise distance: 4.29 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.29 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=3.86 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

