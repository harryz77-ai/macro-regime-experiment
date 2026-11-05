# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-05T03:36:30.609839+00:00
- Latest market date: 2026-11-04
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **39.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.950% | -4.0 bp | -36.0 bp | 30.0 bp | Long-end rate pressure |
| US 30Y yield | 5.320% | 2.0 bp | -34.0 bp | 13.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.27 | -0.90% | -0.95% | 1.45% | Dollar pressure |
| SPY | 766.81 | -0.71% | -1.34% | -0.24% | Broad risk asset |
| QQQ | 691.95 | -4.64% | -8.68% | -3.59% | High-duration growth |
| IWM | 284.02 | 0.97% | 2.28% | -5.39% | Small-cap financing sensitivity |
| TLT | 81.76 | 0.95% | 5.98% | -0.14% | Long-duration bond stress |
| EEM | 61.62 | -2.99% | -8.53% | -5.82% | EM dollar/rate transmission |
| HYG | 77.52 | -0.09% | 0.44% | -1.97% | Credit market proxy |
| HY OAS | 3.40% | 22.0 bp | 37.0 bp | 68.0 bp | Credit spread stress |
| IG OAS | 0.93% | 5.0 bp | 10.0 bp | 14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.62 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.20 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 19.8% | High-rate absorption |
| R1 | 39.6% | Bear steepening + dollar pressure |
| R2 | 11.2% | Credit / sovereign stress spillover |
| R3 | 29.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D; TLT rallied over 20D

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 25.0% | High-rate absorption |
| R1 | 43.0% | Bear steepening + dollar pressure |
| R2 | 18.0% | Credit / sovereign stress spillover |
| R3 | 14.0% | Rate decline / policy repair |

## 7. Risk Alerts

- R1 continuation: **ON**
- R2 upgrade warning: **ON**
- R3 policy-repair signal: **ON**

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

