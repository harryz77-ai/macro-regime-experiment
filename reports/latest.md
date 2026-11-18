# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-18T04:38:25.123848+00:00
- Latest market date: 2026-11-17
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **62.0%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.120% | 26.0 bp | 3.0 bp | 47.0 bp | Long-end rate pressure |
| US 30Y yield | 5.460% | 20.0 bp | 3.0 bp | 27.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.67 | 1.40% | 1.90% | 4.71% | Dollar pressure |
| SPY | 732.44 | -2.33% | -4.76% | -3.83% | Broad risk asset |
| QQQ | 656.95 | -2.64% | -8.46% | -6.89% | High-duration growth |
| IWM | 269.05 | -4.11% | -2.44% | -9.47% | Small-cap financing sensitivity |
| TLT | 79.55 | -1.64% | -0.31% | -2.48% | Long-duration bond stress |
| EEM | 58.27 | -3.80% | -7.98% | -11.86% | EM dollar/rate transmission |
| HYG | 76.63 | -0.71% | 0.26% | -2.39% | Credit market proxy |
| HY OAS | 3.34% | 0.0 bp | 5.0 bp | 65.0 bp | Credit spread stress |
| IG OAS | 0.90% | -1.0 bp | 3.0 bp | 9.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.32 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.21 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.2% | High-rate absorption |
| R1 | 62.0% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

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

