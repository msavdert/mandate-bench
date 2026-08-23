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
| SPY | 18.00 | 0.47 | 80.0% | hold |
| QQQ | 12.60 | 0.52 | 100.0% | decrease |
| IWM | 6.70 | 0.48 | 100.0% | increase |
| EFA | 9.60 | 0.52 | 100.0% | increase |
| EEM | 3.80 | 0.42 | 80.0% | hold |
| TLT | 11.40 | 0.52 | 60.0% | decrease |
| LQD | 7.70 | 0.67 | 80.0% | hold |
| GLD | 9.60 | 1.26 | 80.0% | decrease |
| DBC | 3.10 | 0.74 | 50.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.50 | 0.53 | 50.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.91 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.91 -> not met
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
| SPY | 18.10 | 0.32 | 90.0% | hold |
| QQQ | 14.70 | 0.67 | 80.0% | hold |
| IWM | 5.10 | 0.32 | 90.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 3.90 | 0.32 | 90.0% | hold |
| TLT | 12.10 | 0.57 | 70.0% | hold |
| LQD | 8.00 | 0.00 | 100.0% | hold |
| GLD | 9.20 | 1.32 | 60.0% | decrease |
| DBC | 2.70 | 0.48 | 70.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 13.20 | 1.14 | 60.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.47 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.47 -> not met
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
| SPY | 17.80 | 1.03 | 60.0% | hold |
| QQQ | 13.10 | 0.32 | 100.0% | decrease |
| IWM | 5.10 | 0.32 | 90.0% | hold |
| EFA | 7.90 | 0.32 | 90.0% | hold |
| EEM | 3.90 | 0.32 | 90.0% | hold |
| TLT | 12.90 | 0.88 | 60.0% | increase |
| LQD | 8.00 | 0.00 | 100.0% | hold |
| GLD | 11.30 | 1.34 | 80.0% | increase |
| DBC | 3.00 | 0.00 | 100.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.00 | 0.00 | 100.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.04 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.04 -> not met
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
| SPY | 16.90 | 0.74 | 80.0% | decrease |
| QQQ | 11.80 | 0.63 | 100.0% | decrease |
| IWM | 5.10 | 0.32 | 90.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 12.70 | 0.82 | 50.0% | hold |
| LQD | 8.00 | 0.00 | 100.0% | hold |
| GLD | 13.40 | 0.70 | 100.0% | increase |
| DBC | 4.20 | 0.63 | 90.0% | increase |
| VNQ | 4.90 | 0.32 | 90.0% | hold |
| CASH | 11.00 | 0.82 | 70.0% | decrease |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.58 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.58 -> not met
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
| SPY | 18.00 | 0.00 | 100.0% | hold |
| QQQ | 13.20 | 0.79 | 90.0% | decrease |
| IWM | 6.30 | 0.82 | 80.0% | increase |
| EFA | 8.30 | 0.48 | 70.0% | hold |
| EEM | 3.70 | 0.48 | 70.0% | hold |
| TLT | 11.90 | 0.32 | 90.0% | hold |
| LQD | 7.90 | 0.32 | 90.0% | hold |
| GLD | 11.10 | 1.20 | 70.0% | increase |
| DBC | 3.00 | 0.47 | 80.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 11.60 | 1.17 | 50.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 3.04 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.04 -> not met
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
| SPY | 17.80 | 0.63 | 90.0% | hold |
| QQQ | 12.60 | 1.43 | 90.0% | decrease |
| IWM | 5.40 | 0.70 | 70.0% | hold |
| EFA | 8.10 | 0.32 | 90.0% | hold |
| EEM | 2.80 | 0.79 | 80.0% | decrease |
| TLT | 13.10 | 0.88 | 70.0% | increase |
| LQD | 8.60 | 0.70 | 50.0% | hold |
| GLD | 11.20 | 2.39 | 40.0% | increase |
| DBC | 2.90 | 0.88 | 60.0% | hold |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.50 | 1.51 | 70.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 5.36 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 5.36 -> not met
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
| SPY | 17.80 | 0.42 | 80.0% | hold |
| QQQ | 13.60 | 0.97 | 80.0% | decrease |
| IWM | 5.90 | 0.88 | 60.0% | increase |
| EFA | 8.50 | 0.71 | 60.0% | hold |
| EEM | 3.70 | 0.67 | 50.0% | hold |
| TLT | 12.20 | 1.03 | 50.0% | increase |
| LQD | 8.00 | 0.47 | 80.0% | hold |
| GLD | 10.30 | 1.57 | 40.0% | increase |
| DBC | 3.10 | 0.74 | 50.0% | hold |
| VNQ | 4.80 | 0.63 | 60.0% | hold |
| CASH | 12.10 | 1.37 | 40.0% | decrease |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 5.18 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 5.18 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=2.62 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

