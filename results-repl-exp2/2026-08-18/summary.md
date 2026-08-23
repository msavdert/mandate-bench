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
| SPY | 19.90 | 0.32 | 100.0% | decrease |
| QQQ | 14.70 | 0.67 | 80.0% | hold |
| IWM | 5.50 | 0.85 | 70.0% | hold |
| EFA | 8.60 | 0.97 | 70.0% | hold |
| EEM | 3.50 | 0.53 | 50.0% | hold |
| TLT | 10.10 | 0.32 | 90.0% | hold |
| LQD | 6.60 | 0.84 | 60.0% | hold |
| GLD | 11.80 | 0.42 | 80.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.30 | 1.42 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 3.04 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.04 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 100.0% |
| R2 | CASH < 10% | 100.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 27.90 | 0.32 | 90.0% | hold |
| QQQ | 13.50 | 0.85 | 80.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 3.20 | 0.79 | 60.0% | decrease |
| TLT | 10.50 | 0.53 | 50.0% | hold |
| LQD | 6.10 | 0.32 | 90.0% | hold |
| GLD | 11.00 | 1.05 | 50.0% | decrease |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 6.80 | 1.03 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 0/10 (0.0%)

Mean pairwise distance: 2.49 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=100.0% -> MET
- S2 (mean pairwise distance >= 10 points): 2.49 -> not met
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
| TLT | 10.40 | 0.84 | 80.0% | hold |
| LQD | 6.40 | 0.84 | 80.0% | hold |
| GLD | 12.00 | 0.00 | 100.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.20 | 1.03 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 1.24 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.24 -> not met
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
| GLD | 12.00 | 0.00 | 100.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.00 | 0.00 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 0.00 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 0.00 -> not met
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
| SPY | 19.80 | 0.63 | 100.0% | decrease |
| QQQ | 14.90 | 0.32 | 90.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 3.60 | 0.84 | 80.0% | hold |
| TLT | 10.80 | 1.03 | 60.0% | hold |
| LQD | 6.80 | 0.92 | 50.0% | increase |
| GLD | 12.00 | 0.00 | 100.0% | hold |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.10 | 0.32 | 90.0% | hold |
| CASH | 10.80 | 1.40 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 9/10 (90.0%)

Mean pairwise distance: 2.47 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.47 -> not met
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
| SPY | 19.80 | 0.63 | 100.0% | decrease |
| QQQ | 14.70 | 0.95 | 90.0% | hold |
| IWM | 5.30 | 0.95 | 90.0% | hold |
| EFA | 8.40 | 0.97 | 80.0% | hold |
| EEM | 2.70 | 1.49 | 50.0% | decrease |
| TLT | 10.20 | 1.14 | 70.0% | hold |
| LQD | 6.60 | 0.97 | 70.0% | hold |
| GLD | 12.60 | 1.35 | 50.0% | hold |
| DBC | 3.30 | 0.95 | 70.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.40 | 1.65 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 5.13 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 5.13 -> not met
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
| QQQ | 14.70 | 0.48 | 70.0% | hold |
| IWM | 5.80 | 1.14 | 60.0% | hold |
| EFA | 9.10 | 1.10 | 60.0% | increase |
| EEM | 2.80 | 1.32 | 60.0% | decrease |
| TLT | 9.90 | 0.32 | 90.0% | hold |
| LQD | 6.10 | 0.32 | 90.0% | hold |
| GLD | 11.80 | 0.42 | 80.0% | hold |
| DBC | 3.10 | 0.32 | 90.0% | hold |
| VNQ | 5.00 | 0.47 | 80.0% | hold |
| CASH | 11.70 | 1.34 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 3.62 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.62 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): insufficient nonzero data -> not met

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

