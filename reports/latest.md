# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-07T02:35:41.200221+00:00
- Latest market date: 2026-10-06
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **79.3%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.310% | 7.0 bp | 53.0 bp | 75.0 bp | Long-end rate pressure |
| US 30Y yield | 5.660% | 10.0 bp | 42.0 bp | 60.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.05 | 0.67% | 3.25% | 0.76% | Dollar pressure |
| SPY | 779.09 | 1.95% | 1.97% | 4.25% | Broad risk asset |
| QQQ | 759.66 | 2.94% | 5.86% | 6.84% | High-duration growth |
| IWM | 281.34 | 0.84% | -4.27% | -3.89% | Small-cap financing sensitivity |
| TLT | 77.28 | -0.82% | -5.61% | -6.87% | Long-duration bond stress |
| EEM | 68.27 | 1.29% | -0.81% | 5.84% | EM dollar/rate transmission |
| HYG | 77.27 | 0.33% | -1.90% | -1.39% | Credit market proxy |
| HY OAS | 3.12% | 10.0 bp | 44.0 bp | 43.0 bp | Credit spread stress |
| IG OAS | 0.84% | 1.0 bp | 3.0 bp | 6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -6.24 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.78 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 9.0% | High-rate absorption |
| R1 | 79.3% | Bear steepening + dollar pressure |
| R2 | 6.5% | Credit / sovereign stress spillover |
| R3 | 5.1% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: no strong evidence
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

