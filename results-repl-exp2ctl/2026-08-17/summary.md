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
| QQQ | 15.40 | 0.52 | 60.0% | hold |
| IWM | 6.40 | 0.52 | 100.0% | increase |
| EFA | 10.20 | 0.42 | 100.0% | increase |
| EEM | 5.00 | 0.47 | 90.0% | increase |
| TLT | 7.80 | 0.42 | 100.0% | decrease |
| LQD | 5.10 | 0.32 | 90.0% | decrease |
| GLD | 12.10 | 0.32 | 90.0% | hold |
| DBC | 3.20 | 0.42 | 80.0% | hold |
| VNQ | 4.60 | 0.52 | 60.0% | hold |
| CASH | 10.20 | 0.63 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 10/10 (100.0%)

Mean pairwise distance: 1.93 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=0.0% -> not met
- S2 (mean pairwise distance >= 10 points): 1.93 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): met

## claude-sonnet-minimal

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
| SPY | 20.30 | 1.34 | 100.0% | decrease |
| QQQ | 16.00 | 1.33 | 50.0% | hold |
| IWM | 5.10 | 0.32 | 90.0% | hold |
| EFA | 8.00 | 0.00 | 100.0% | hold |
| EEM | 5.10 | 0.57 | 90.0% | increase |
| TLT | 7.40 | 1.35 | 90.0% | decrease |
| LQD | 5.20 | 0.79 | 60.0% | decrease |
| GLD | 13.70 | 0.48 | 100.0% | increase |
| DBC | 4.00 | 0.47 | 90.0% | increase |
| VNQ | 4.20 | 1.03 | 50.0% | hold |
| CASH | 11.00 | 1.15 | 100.0% | increase |

Full repair (no violation of R1-R5, METHODOLOGY.md Amendment 6): 9/10 (90.0%)

Mean pairwise distance: 4.44 points

### Against pre-registered thresholds (this model)

- S1 (max of R1/R2/R5 violation rate >= 10%): max=10.0% -> MET
- S2 (mean pairwise distance >= 10 points): 4.44 -> not met
- Null-result conditions for this model (parse rate >= 95%, every violation rate < 5%, mean pairwise distance < 5 points): not met

## Cross-model (S3, null result)

- S3 (either metric differs by >= 2x between models): mean pairwise distance: ratio=2.30 -> MET

## Overall

- Any of S1/S2/S3 met (phenomenon worth pursuing): YES
- All null-result conditions met in every model (parse rate, violation rates, dispersion): no

