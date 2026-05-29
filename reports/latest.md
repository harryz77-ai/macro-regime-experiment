# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-05-29T11:56:56.948696+00:00
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
| US 10Y yield | 4.480% | -19.0 bp | 12.0 bp | 42.0 bp | Long-end rate pressure |
| US 30Y yield | 5.010% | -17.0 bp | 7.0 bp | 31.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.04 | -0.15% | 0.98% | 0.28% | Dollar pressure |
| SPY | 754.60 | 1.80% | 6.05% | 11.22% | Broad risk asset |
| QQQ | 735.60 | 3.15% | 11.19% | 22.43% | High-duration growth |
| IWM | 292.03 | 4.34% | 7.33% | 12.85% | Small-cap financing sensitivity |
| TLT | 85.74 | 2.18% | 0.42% | -3.39% | Long-duration bond stress |
| EEM | 68.61 | 4.81% | 9.44% | 17.44% | EM dollar/rate transmission |
| HYG | 80.23 | 0.46% | 0.65% | 1.15% | Credit market proxy |
| HY OAS | 2.71% | -9.0 bp | -11.0 bp | -26.0 bp | Credit spread stress |
| IG OAS | 0.74% | -1.0 bp | -7.0 bp | -8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.29 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 3.40 pp | n/a | EM relative stress |

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

