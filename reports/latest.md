# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-05-30T08:41:45.400701+00:00
- Latest market date: 2026-05-29
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **62.7%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.450% | -12.0 bp | 3.0 bp | 36.0 bp | Long-end rate pressure |
| US 30Y yield | 4.980% | -13.0 bp | 0.0 bp | 26.0 bp | Term premium / fiscal supply pressure |
| DXY | 98.91 | -0.28% | 0.85% | 0.14% | Dollar pressure |
| SPY | 756.48 | 1.85% | 5.26% | 10.72% | Broad risk asset |
| QQQ | 738.31 | 3.33% | 10.57% | 21.04% | High-duration growth |
| IWM | 290.43 | 2.81% | 4.48% | 11.15% | Small-cap financing sensitivity |
| TLT | 85.76 | 1.83% | 0.53% | -3.06% | Long-duration bond stress |
| EEM | 68.60 | 3.89% | 7.20% | 16.17% | EM dollar/rate transmission |
| HYG | 80.31 | 0.51% | 0.44% | 0.90% | Credit market proxy |
| HY OAS | 2.72% | -6.0 bp | -11.0 bp | -28.0 bp | Credit spread stress |
| IG OAS | 0.73% | -2.0 bp | -8.0 bp | -9.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.78 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.94 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 62.7% | High-rate absorption |
| R1 | 17.5% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
| R3 | 13.7% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

