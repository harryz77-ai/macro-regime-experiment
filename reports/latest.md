# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-15T01:39:39.962403+00:00
- Latest market date: 2026-10-14
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **76.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.210% | -10.0 bp | 24.0 bp | 66.0 bp | Long-end rate pressure |
| US 30Y yield | 5.560% | -10.0 bp | 22.0 bp | 50.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.05 | -0.18% | 1.74% | 0.86% | Dollar pressure |
| SPY | 769.60 | -0.98% | 2.32% | 3.10% | Broad risk asset |
| QQQ | 728.95 | -3.80% | 3.55% | 2.93% | High-duration growth |
| IWM | 271.37 | -2.28% | -4.42% | -8.25% | Small-cap financing sensitivity |
| TLT | 78.89 | 2.26% | -2.07% | -4.58% | Long-duration bond stress |
| EEM | 64.39 | -4.42% | -2.02% | -1.45% | EM dollar/rate transmission |
| HYG | 76.81 | -0.48% | -1.62% | -2.13% | Credit market proxy |
| HY OAS | 3.16% | 13.0 bp | 40.0 bp | 47.0 bp | Credit spread stress |
| IG OAS | 0.83% | 0.0 bp | 3.0 bp | 5.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -6.74 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.34 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 9.9% | High-rate absorption |
| R1 | 76.7% | Bear steepening + dollar pressure |
| R2 | 7.4% | Credit / sovereign stress spillover |
| R3 | 6.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: no strong evidence
- **R1**: 10Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

