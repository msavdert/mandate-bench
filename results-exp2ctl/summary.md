# Mandate Bench - Results Summary

See METHODOLOGY.md for metric definitions and pre-registered
success criteria (S1/S2/S3, null-result criteria).

## claude-opus-minimal

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
| IWM | 5.80 | 0.63 | 70.0% | increase |
| EFA | 10.20 | 0.42 | 100.0% | increase |
| EEM | 3.90 | 0.32 | 90.0% | hold |
| TLT | 8.80 | 0.79 | 80.0% | decrease |
| LQD | 5.70 | 0.48 | 70.0% | hold |
| GLD | 12.20 | 0.42 | 80.0% | hold |
| DBC | 3.50 | 0.53 | 50.0% | hold |
| VNQ | 5.00 | 0.47 | 80.0% | hold |
| CASH | 10.20 | 0.42 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.36 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.36 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet-minimal

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 30.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 21.30 | 2.41 | 100.0% | decrease |
| QQQ | 13.50 | 0.97 | 80.0% | decrease |
| IWM | 5.00 | 0.47 | 80.0% | hold |
| EFA | 8.50 | 0.71 | 60.0% | increase |
| EEM | 4.10 | 0.57 | 70.0% | hold |
| TLT | 8.60 | 0.97 | 80.0% | decrease |
| LQD | 5.70 | 0.48 | 70.0% | hold |
| GLD | 13.30 | 1.06 | 80.0% | increase |
| DBC | 3.50 | 0.53 | 50.0% | increase |
| VNQ | 4.70 | 0.48 | 70.0% | hold |
| CASH | 11.80 | 1.69 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 7/10 (70.0%)

Mean pairwise distance: 5.44 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=30.0% -> MET
- S2 (mean pairwise distance >= 10 points): 5.44 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=2.31 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

