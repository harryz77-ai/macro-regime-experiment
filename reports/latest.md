# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-11T02:55:14.271428+00:00
- Latest market date: 2026-11-10
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **46.0%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.880% | -3.0 bp | -36.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.260% | -2.0 bp | -34.0 bp | 5.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.26 | 0.38% | 0.08% | 2.63% | Dollar pressure |
| SPY | 749.92 | -0.59% | -3.61% | -2.70% | Broad risk asset |
| QQQ | 674.76 | -1.54% | -9.25% | -7.45% | High-duration growth |
| IWM | 280.58 | 0.28% | 1.40% | -7.48% | Small-cap financing sensitivity |
| TLT | 80.88 | -0.28% | 3.20% | 0.21% | Long-duration bond stress |
| EEM | 60.57 | -0.87% | -7.86% | -10.03% | EM dollar/rate transmission |
| HYG | 77.18 | 0.26% | 0.12% | -2.09% | Credit market proxy |
| HY OAS | 3.34% | -9.0 bp | 23.0 bp | 64.0 bp | Credit spread stress |
| IG OAS | 0.91% | -3.0 bp | 8.0 bp | 10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.01 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.25 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 22.7% | High-rate absorption |
| R1 | 46.0% | Bear steepening + dollar pressure |
| R2 | 12.5% | Credit / sovereign stress spillover |
| R3 | 18.8% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D

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

