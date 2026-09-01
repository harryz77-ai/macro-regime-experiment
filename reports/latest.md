# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-01T01:57:49.508948+00:00
- Latest market date: 2026-08-31
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **59.1%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.730% | -1.0 bp | -2.0 bp | 24.0 bp | Long-end rate pressure |
| US 30Y yield | 5.220% | -5.0 bp | -5.0 bp | 23.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.46 | 0.46% | -0.50% | 0.05% | Dollar pressure |
| SPY | 767.05 | 0.47% | 1.24% | 1.58% | Broad risk asset |
| QQQ | 716.76 | 1.48% | 2.38% | -3.11% | High-duration growth |
| IWM | 293.93 | -1.36% | -0.77% | 0.90% | Small-cap financing sensitivity |
| TLT | 82.52 | -0.05% | 0.40% | -2.74% | Long-duration bond stress |
| EEM | 67.02 | 1.38% | 4.20% | -2.51% | EM dollar/rate transmission |
| HYG | 79.81 | 0.14% | 0.63% | 0.93% | Credit market proxy |
| HY OAS | 2.60% | -10.0 bp | -25.0 bp | -16.0 bp | Credit spread stress |
| IG OAS | 0.79% | -2.0 bp | 0.0 bp | 5.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.01 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.96 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 59.1% | High-rate absorption |
| R1 | 26.7% | Bear steepening + dollar pressure |
| R2 | 5.7% | Credit / sovereign stress spillover |
| R3 | 8.5% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 55.0% | High-rate absorption |
| R1 | 25.0% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
| R3 | 14.0% | Rate decline / policy repair |

## 7. Risk Alerts

- R1 continuation: **ON**
- R2 upgrade warning: **not confirmed**
- R3 policy-repair signal: **not confirmed**

## 8. Interpretation

### Verified market data

The report uses FRED for US Treasury yields and credit OAS series, and Yahoo Finance for ETF/index market proxies where available.

### Computed indicators

The system computes 5D, 20D, and 60D changes. ETF/index moves are percentage returns. Yield and spread moves are basis-point changes.

### Model inference

The top regime is the highest posterior probability regime after combining cross-asset signal probability with the Markov transition prior when a previous regime is provided.

### Judgment call

Do not upgrade to R2 from rates and equity weakness alone. R2 requires credit-spread stress, sovereign-spread stress, or synchronized deleveraging across equities, EM, credit, and high-duration assets.

## 9. Next Data to Watch

1. HY OAS 20D change
2. HYG 20D return
3. DXY level and 20D return
4. IWM/SPY and EEM/SPY relative performance
5. US 10Y and 30Y yield levels

