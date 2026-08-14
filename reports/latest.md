# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-14T00:07:15.911217+00:00
- Latest market date: 2026-08-13
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
| US 10Y yield | 4.680% | 5.0 bp | 13.0 bp | 9.0 bp | Long-end rate pressure |
| US 30Y yield | 5.240% | 7.0 bp | 16.0 bp | 12.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.92 | -0.05% | -1.34% | 1.46% | Dollar pressure |
| SPY | 777.88 | 1.21% | 3.62% | 5.58% | Broad risk asset |
| QQQ | 732.07 | 2.44% | 3.70% | 3.82% | High-duration growth |
| IWM | 303.50 | 1.76% | 2.68% | 10.24% | Small-cap financing sensitivity |
| TLT | 82.59 | 0.08% | -1.53% | -0.00% | Long-duration bond stress |
| EEM | 66.68 | 2.55% | 1.69% | 3.01% | EM dollar/rate transmission |
| HYG | 79.79 | 0.42% | 0.62% | 1.39% | Credit market proxy |
| HY OAS | 2.71% | -4.0 bp | 0.0 bp | -7.0 bp | Credit spread stress |
| IG OAS | 0.79% | 1.0 bp | 0.0 bp | 4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.94 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.93 pp | n/a | EM relative stress |

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

