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
| SPY | 17.50 | 0.53 | 50.0% | hold |
| QQQ | 12.00 | 0.00 | 100.0% | decrease |
| IWM | 5.30 | 0.48 | 70.0% | hold |
| EFA | 9.00 | 0.47 | 90.0% | increase |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 9.90 | 0.32 | 100.0% | decrease |
| LQD | 7.70 | 0.48 | 70.0% | hold |
| GLD | 12.10 | 0.57 | 100.0% | increase |
| DBC | 5.20 | 0.42 | 100.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.30 | 0.67 | 50.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 1.87 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.87 -> not met
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
| SPY | 16.40 | 0.70 | 90.0% | decrease |
| QQQ | 13.20 | 0.42 | 100.0% | decrease |
| IWM | 4.50 | 0.53 | 50.0% | hold |
| EFA | 7.80 | 0.42 | 80.0% | hold |
| EEM | 4.10 | 0.32 | 90.0% | hold |
| TLT | 11.20 | 0.79 | 60.0% | decrease |
| LQD | 8.00 | 0.00 | 100.0% | hold |
| GLD | 12.80 | 0.42 | 100.0% | increase |
| DBC | 4.40 | 0.84 | 80.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.60 | 1.07 | 60.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.76 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.76 -> not met
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
| SPY | 16.20 | 0.92 | 90.0% | decrease |
| QQQ | 13.40 | 1.07 | 80.0% | decrease |
| IWM | 4.90 | 0.32 | 90.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 11.20 | 1.03 | 60.0% | hold |
| LQD | 7.80 | 0.63 | 90.0% | hold |
| GLD | 12.50 | 0.97 | 100.0% | increase |
| DBC | 4.70 | 0.48 | 100.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.30 | 0.67 | 80.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 3.02 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.02 -> not met
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
| SPY | 17.10 | 0.99 | 50.0% | decrease |
| QQQ | 12.30 | 0.48 | 100.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.00 | 0.00 | 100.0% | decrease |
| LQD | 8.00 | 0.00 | 100.0% | hold |
| GLD | 13.00 | 0.47 | 100.0% | increase |
| DBC | 5.30 | 0.48 | 100.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.30 | 0.82 | 60.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 1.64 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.64 -> not met
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
| SPY | 18.00 | 0.00 | 100.0% | hold |
| QQQ | 13.40 | 0.70 | 90.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.20 | 0.42 | 100.0% | decrease |
| LQD | 7.80 | 0.42 | 80.0% | hold |
| GLD | 11.90 | 0.74 | 100.0% | increase |
| DBC | 4.40 | 0.52 | 100.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.50 | 0.97 | 70.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 9/10 (90.0%)

Mean pairwise distance: 1.80 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.80 -> not met
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
| SPY | 17.10 | 0.88 | 60.0% | decrease |
| QQQ | 12.20 | 0.63 | 100.0% | decrease |
| IWM | 4.70 | 0.48 | 70.0% | hold |
| EFA | 8.50 | 1.08 | 60.0% | hold |
| EEM | 3.90 | 0.57 | 70.0% | hold |
| TLT | 10.20 | 0.63 | 100.0% | decrease |
| LQD | 7.00 | 1.33 | 70.0% | decrease |
| GLD | 13.20 | 0.79 | 100.0% | increase |
| DBC | 5.70 | 1.34 | 100.0% | increase |
| VNQ | 4.60 | 0.70 | 70.0% | hold |
| CASH | 12.90 | 1.60 | 50.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 5.20 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 5.20 -> not met
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
| SPY | 18.10 | 0.32 | 90.0% | hold |
| QQQ | 13.70 | 0.95 | 80.0% | decrease |
| IWM | 5.30 | 0.67 | 80.0% | hold |
| EFA | 8.80 | 0.79 | 60.0% | increase |
| EEM | 4.20 | 0.42 | 80.0% | hold |
| TLT | 9.90 | 0.32 | 100.0% | decrease |
| LQD | 7.50 | 0.71 | 60.0% | hold |
| GLD | 11.10 | 1.10 | 70.0% | increase |
| DBC | 4.10 | 0.57 | 90.0% | increase |
| VNQ | 5.10 | 0.32 | 90.0% | hold |
| CASH | 12.10 | 1.29 | 40.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 9/10 (90.0%)

Mean pairwise distance: 3.74 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.74 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=3.16 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

