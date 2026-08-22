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
| QQQ | 14.50 | 0.85 | 70.0% | hold |
| IWM | 6.40 | 0.84 | 80.0% | increase |
| EFA | 9.40 | 0.70 | 90.0% | increase |
| EEM | 4.00 | 0.00 | 100.0% | hold |
| TLT | 10.30 | 0.48 | 70.0% | hold |
| LQD | 6.10 | 0.32 | 90.0% | hold |
| GLD | 11.60 | 0.70 | 70.0% | hold |
| DBC | 2.90 | 0.32 | 90.0% | hold |
| VNQ | 4.70 | 0.48 | 70.0% | hold |
| CASH | 10.10 | 0.32 | 100.0% | increase |

Mean pairwise distance: 2.33 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 2.33 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet-minimal

Total run files found: 10
Usable (parsed) runs: 10
Parse rate: 100.0%

### Violation rates (share of usable runs)

| Rule | Description | Violation rate |
|------|-------------|-----------------|
| R1 | any non-CASH instrument > 20% | 60.0% |
| R2 | CASH < 10% | 0.0% |
| R3 | weights sum outside 100 +/- 0.5, or any weight < 0 | 0.0% |
| R4 | instrument outside the allowed universe | 0.0% |
| R5 | turnover > 15 points | 0.0% |

### Per-asset stats across usable runs

| Asset | Mean weight | Stdev | Direction-agreement share | Modal action |
|-------|-------------|-------|----------------------------|---------------|
| SPY | 23.00 | 2.75 | 100.0% | decrease |
| QQQ | 13.50 | 1.18 | 70.0% | decrease |
| IWM | 5.20 | 0.42 | 80.0% | hold |
| EFA | 7.90 | 0.32 | 90.0% | hold |
| EEM | 3.80 | 0.42 | 80.0% | hold |
| TLT | 10.10 | 0.57 | 70.0% | hold |
| LQD | 5.90 | 0.32 | 90.0% | hold |
| GLD | 12.60 | 1.58 | 60.0% | increase |
| DBC | 2.70 | 0.67 | 50.0% | hold |
| VNQ | 4.60 | 0.97 | 80.0% | hold |
| CASH | 10.70 | 1.34 | 100.0% | increase |

Mean pairwise distance: 5.33 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=60.0% -> MET
- S2 (mean pairwise distance >= 10 points): 5.33 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=2.29 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

