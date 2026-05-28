# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-05-28T12:48:05.102672+00:00
- Latest market date: 2026-05-28
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **52.2%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.500% | -11.0 bp | 15.0 bp | 45.0 bp | Long-end rate pressure |
| US 30Y yield | 5.030% | -11.0 bp | 9.0 bp | 33.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.20 | 0.09% | 0.28% | 0.15% | Dollar pressure |
| SPY | 750.46 | 2.28% | 5.45% | 9.63% | Broad risk asset |
| QQQ | 729.45 | 3.98% | 10.93% | 20.11% | High-duration growth |
| IWM | 290.37 | 6.36% | 6.01% | 10.26% | Small-cap financing sensitivity |
| TLT | 85.30 | 2.75% | -0.87% | -4.08% | Long-duration bond stress |
| EEM | 68.39 | 6.43% | 8.57% | 11.20% | EM dollar/rate transmission |
| HYG | 80.13 | 0.98% | 0.19% | 0.82% | Credit market proxy |
| HY OAS | 2.72% | -14.0 bp | -13.0 bp | -36.0 bp | Credit spread stress |
| IG OAS | 0.74% | -2.0 bp | -7.0 bp | -10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.56 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 3.13 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 52.2% | High-rate absorption |
| R1 | 23.8% | Bear steepening + dollar pressure |
| R2 | 10.2% | Credit / sovereign stress spillover |
| R3 | 13.7% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 25.0% | High-rate absorption |
| R1 | 43.0% | Bear steepening + dollar pressure |
| R2 | 18.0% | Credit / sovereign stress spillover |
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

