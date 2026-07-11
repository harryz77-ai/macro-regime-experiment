# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-11T00:56:42.075928+00:00
- Latest market date: 2026-07-10
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **43.8%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.540% | 6.0 bp | 1.0 bp | 24.0 bp | Long-end rate pressure |
| US 30Y yield | 5.050% | 8.0 bp | 4.0 bp | 15.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.96 | 0.10% | 1.02% | 2.90% | Dollar pressure |
| SPY | 754.95 | 1.37% | 4.34% | 8.99% | Broad risk asset |
| QQQ | 725.51 | 1.81% | 4.70% | 15.54% | High-duration growth |
| IWM | 295.99 | -0.53% | 5.19% | 10.41% | Small-cap financing sensitivity |
| TLT | 84.47 | -1.22% | -0.12% | -2.04% | Long-duration bond stress |
| EEM | 66.90 | 1.83% | 4.00% | 8.05% | EM dollar/rate transmission |
| HYG | 79.71 | 0.00% | 0.77% | 0.51% | Credit market proxy |
| HY OAS | 2.70% | -5.0 bp | -8.0 bp | -13.0 bp | Credit spread stress |
| IG OAS | 0.76% | 1.0 bp | 1.0 bp | -4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.85 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.34 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 43.8% | High-rate absorption |
| R1 | 33.3% | Bear steepening + dollar pressure |
| R2 | 7.0% | Credit / sovereign stress spillover |
| R3 | 15.9% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

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

