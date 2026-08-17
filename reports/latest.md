# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-17T23:46:33.144377+00:00
- Latest market date: 2026-08-17
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **50.2%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.680% | 3.0 bp | 13.0 bp | 1.0 bp | Long-end rate pressure |
| US 30Y yield | 5.250% | 6.0 bp | 19.0 bp | 7.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.58 | -0.23% | -1.40% | 0.48% | Dollar pressure |
| SPY | 772.67 | -0.05% | 4.12% | 4.51% | Broad risk asset |
| QQQ | 729.87 | 1.25% | 4.86% | 2.46% | High-duration growth |
| IWM | 304.06 | 1.36% | 4.02% | 8.90% | Small-cap financing sensitivity |
| TLT | 81.35 | -0.87% | -2.64% | -1.92% | Long-duration bond stress |
| EEM | 67.32 | 3.30% | 5.92% | 3.38% | EM dollar/rate transmission |
| HYG | 79.61 | 0.16% | 0.40% | 1.15% | Credit market proxy |
| HY OAS | 2.67% | -3.0 bp | -6.0 bp | -7.0 bp | Credit spread stress |
| IG OAS | 0.80% | 2.0 bp | 1.0 bp | 6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.10 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.79 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 50.2% | High-rate absorption |
| R1 | 22.7% | Bear steepening + dollar pressure |
| R2 | 8.3% | Credit / sovereign stress spillover |
| R3 | 18.8% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
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

