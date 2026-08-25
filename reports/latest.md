# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-25T23:48:55.011661+00:00
- Latest market date: 2026-08-25
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
| US 10Y yield | 4.700% | -2.0 bp | 5.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.230% | -8.0 bp | 11.0 bp | 25.0 bp | Term premium / fiscal supply pressure |
| DXY | 98.90 | -0.75% | -2.44% | -0.01% | Dollar pressure |
| SPY | 765.91 | -0.20% | 3.38% | 1.51% | Broad risk asset |
| QQQ | 710.72 | -0.95% | 5.22% | -3.63% | High-duration growth |
| IWM | 299.23 | -0.33% | 2.00% | 3.28% | Small-cap financing sensitivity |
| TLT | 83.47 | 2.22% | -0.51% | -1.53% | Long-duration bond stress |
| EEM | 67.25 | 2.92% | 7.84% | -1.46% | EM dollar/rate transmission |
| HYG | 79.92 | 0.49% | 1.12% | 0.98% | Credit market proxy |
| HY OAS | 2.69% | -1.0 bp | -12.0 bp | -3.0 bp | Credit spread stress |
| IG OAS | 0.81% | 0.0 bp | 0.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.38 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 4.46 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 43.8% | High-rate absorption |
| R1 | 19.8% | Bear steepening + dollar pressure |
| R2 | 7.0% | Credit / sovereign stress spillover |
| R3 | 29.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: DXY weakened over 20D; SPY and QQQ rallied over 20D

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

