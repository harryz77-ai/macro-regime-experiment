# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-20T23:50:11.123283+00:00
- Latest market date: 2026-08-20
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
| US 10Y yield | 4.650% | -3.0 bp | -2.0 bp | 9.0 bp | Long-end rate pressure |
| US 30Y yield | 5.190% | -5.0 bp | 4.0 bp | 12.0 bp | Term premium / fiscal supply pressure |
| DXY | 98.84 | -1.12% | -2.55% | -0.33% | Dollar pressure |
| SPY | 762.60 | -1.96% | 3.31% | 1.86% | Broad risk asset |
| QQQ | 710.93 | -2.89% | 2.74% | -2.54% | High-duration growth |
| IWM | 297.67 | -1.92% | 1.91% | 2.71% | Small-cap financing sensitivity |
| TLT | 82.34 | -0.30% | -0.60% | -2.11% | Long-duration bond stress |
| EEM | 66.62 | -0.09% | 3.13% | -2.10% | EM dollar/rate transmission |
| HYG | 79.56 | -0.29% | 0.90% | 0.68% | Credit market proxy |
| HY OAS | 2.73% | 2.0 bp | 5.0 bp | 1.0 bp | Credit spread stress |
| IG OAS | 0.81% | 2.0 bp | 3.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.40 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.18 pp | n/a | EM relative stress |

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
- **R3**: DXY weakened over 20D

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

