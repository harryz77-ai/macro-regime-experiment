# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-14T23:47:13.433489+00:00
- Latest market date: 2026-08-14
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
| US 10Y yield | 4.630% | -6.0 bp | 6.0 bp | 2.0 bp | Long-end rate pressure |
| US 30Y yield | 5.210% | -1.0 bp | 12.0 bp | 7.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.64 | 0.04% | -1.11% | 0.34% | Dollar pressure |
| SPY | 776.34 | 0.40% | 4.45% | 6.08% | Broad risk asset |
| QQQ | 731.07 | 1.11% | 5.14% | 4.33% | High-duration growth |
| IWM | 305.09 | 1.17% | 3.76% | 12.02% | Small-cap financing sensitivity |
| TLT | 82.04 | -0.87% | -2.54% | -0.02% | Long-duration bond stress |
| EEM | 66.61 | 1.48% | 5.25% | 4.20% | EM dollar/rate transmission |
| HYG | 79.71 | 0.13% | 0.56% | 1.93% | Credit market proxy |
| HY OAS | 2.71% | 0.0 bp | 0.0 bp | -3.0 bp | Credit spread stress |
| IG OAS | 0.79% | 1.0 bp | 1.0 bp | 5.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.69 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 0.80 pp | n/a | EM relative stress |

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

