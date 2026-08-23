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
| QQQ | 14.50 | 0.71 | 60.0% | hold |
| IWM | 6.50 | 0.71 | 90.0% | increase |
| EFA | 9.90 | 0.32 | 100.0% | increase |
| EEM | 3.20 | 0.63 | 70.0% | decrease |
| TLT | 10.00 | 0.47 | 80.0% | hold |
| LQD | 6.20 | 0.63 | 90.0% | hold |
| GLD | 11.40 | 0.70 | 50.0% | hold |
| DBC | 3.10 | 0.32 | 90.0% | hold |
| VNQ | 5.20 | 0.42 | 80.0% | hold |
| CASH | 10.00 | 0.00 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 2.22 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.22 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet-minimal

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 20.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 20.90 | 1.91 | 100.0% | decrease |
| QQQ | 13.10 | 0.74 | 100.0% | decrease |
| IWM | 5.00 | 0.00 | 100.0% | hold |
| EFA | 8.00 | 0.47 | 80.0% | hold |
| EEM | 3.00 | 0.67 | 80.0% | decrease |
| TLT | 11.00 | 1.05 | 60.0% | increase |
| LQD | 6.40 | 0.70 | 70.0% | hold |
| GLD | 11.00 | 0.82 | 70.0% | decrease |
| DBC | 3.20 | 0.42 | 80.0% | hold |
| VNQ | 5.10 | 0.32 | 90.0% | hold |
| CASH | 13.30 | 2.06 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 8/10 (80.0%)

Mean pairwise distance: 4.64 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=20.0% -> MET
- S2 (mean pairwise distance >= 10 points): 4.64 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=2.09 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

