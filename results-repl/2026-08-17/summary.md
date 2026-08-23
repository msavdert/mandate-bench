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
| SPY | 18.20 | 0.42 | 80.0% | hold |
| QQQ | 15.10 | 0.32 | 90.0% | hold |
| IWM | 7.10 | 0.32 | 100.0% | increase |
| EFA | 10.70 | 0.67 | 100.0% | increase |
| EEM | 4.60 | 0.52 | 60.0% | increase |
| TLT | 7.80 | 0.63 | 100.0% | decrease |
| LQD | 6.20 | 0.42 | 100.0% | decrease |
| GLD | 10.00 | 0.00 | 100.0% | hold |
| DBC | 3.60 | 0.52 | 60.0% | increase |
| VNQ | 4.50 | 0.53 | 50.0% | hold |
| CASH | 12.20 | 0.63 | 60.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.40 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.40 -> not met
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
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 4.80 | 0.79 | 60.0% | increase |
| TLT | 9.70 | 1.06 | 90.0% | decrease |
| LQD | 7.50 | 0.85 | 70.0% | hold |
| GLD | 11.90 | 0.88 | 90.0% | increase |
| DBC | 4.20 | 0.63 | 90.0% | increase |
| VNQ | 4.80 | 0.63 | 90.0% | hold |
| CASH | 11.10 | 0.99 | 70.0% | decrease |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.98 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.98 -> not met
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
| SPY | 17.90 | 0.32 | 90.0% | hold |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.20 | 0.63 | 90.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 5.10 | 0.88 | 70.0% | increase |
| TLT | 9.70 | 0.67 | 100.0% | decrease |
| LQD | 6.70 | 0.82 | 80.0% | decrease |
| GLD | 11.50 | 0.71 | 90.0% | increase |
| DBC | 3.90 | 0.88 | 60.0% | increase |
| VNQ | 5.00 | 0.00 | 100.0% | hold |
| CASH | 12.00 | 0.00 | 100.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.40 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.40 -> not met
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
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 10.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 17.80 | 0.42 | 80.0% | hold |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 5.80 | 0.42 | 100.0% | increase |
| TLT | 9.10 | 0.32 | 100.0% | decrease |
| LQD | 6.60 | 0.52 | 100.0% | decrease |
| GLD | 11.80 | 0.42 | 100.0% | increase |
| DBC | 4.70 | 0.48 | 100.0% | increase |
| VNQ | 4.10 | 0.57 | 80.0% | decrease |
| CASH | 12.00 | 0.67 | 60.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 9/10 (90.0%)

Mean pairwise distance: 1.77 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.77 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

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
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.80 | 0.79 | 60.0% | increase |
| EFA | 8.20 | 0.42 | 80.0% | hold |
| EEM | 6.00 | 0.94 | 90.0% | increase |
| TLT | 8.90 | 0.88 | 100.0% | decrease |
| LQD | 6.80 | 0.92 | 80.0% | decrease |
| GLD | 10.50 | 0.53 | 50.0% | hold |
| DBC | 3.60 | 0.84 | 60.0% | hold |
| VNQ | 4.90 | 0.99 | 70.0% | hold |
| CASH | 12.20 | 1.03 | 80.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 9/10 (90.0%)

Mean pairwise distance: 3.74 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 3.74 -> not met
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
| SPY | 18.20 | 1.99 | 50.0% | increase |
| QQQ | 15.30 | 1.34 | 40.0% | increase |
| IWM | 5.10 | 0.57 | 70.0% | hold |
| EFA | 8.70 | 1.57 | 50.0% | increase |
| EEM | 6.70 | 0.82 | 100.0% | increase |
| TLT | 7.90 | 1.10 | 100.0% | decrease |
| LQD | 5.80 | 0.63 | 100.0% | decrease |
| GLD | 12.40 | 1.71 | 100.0% | increase |
| DBC | 4.90 | 0.88 | 100.0% | increase |
| VNQ | 3.80 | 0.63 | 90.0% | decrease |
| CASH | 11.20 | 1.40 | 50.0% | decrease |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 6.62 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 6.62 -> not met
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
| SPY | 18.00 | 0.00 | 100.0% | hold |
| QQQ | 15.00 | 0.00 | 100.0% | hold |
| IWM | 5.50 | 0.71 | 60.0% | hold |
| EFA | 8.30 | 0.67 | 80.0% | hold |
| EEM | 5.70 | 0.67 | 100.0% | increase |
| TLT | 8.50 | 1.35 | 100.0% | decrease |
| LQD | 6.60 | 0.70 | 90.0% | decrease |
| GLD | 11.00 | 1.49 | 50.0% | increase |
| DBC | 4.20 | 0.92 | 70.0% | increase |
| VNQ | 4.80 | 0.42 | 80.0% | hold |
| CASH | 12.40 | 1.17 | 50.0% | hold |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 4.36 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 4.36 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=3.75 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

