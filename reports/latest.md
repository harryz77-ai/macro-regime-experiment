# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-30T02:16:43.989610+00:00
- Latest market date: 2026-09-29
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **78.5%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.240% | 28.0 bp | 51.0 bp | 75.0 bp | Long-end rate pressure |
| US 30Y yield | 5.560% | 27.0 bp | 34.0 bp | 58.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.38 | 0.77% | 1.96% | 0.52% | Dollar pressure |
| SPY | 764.20 | -1.19% | -0.12% | 1.97% | Broad risk asset |
| QQQ | 737.93 | -1.27% | 3.06% | 2.20% | High-duration growth |
| IWM | 279.01 | -2.86% | -4.83% | -6.41% | Small-cap financing sensitivity |
| TLT | 78.23 | -4.31% | -4.84% | -7.73% | Long-duration bond stress |
| EEM | 67.40 | -2.46% | 0.57% | -0.25% | EM dollar/rate transmission |
| HYG | 77.36 | -1.67% | -2.54% | -2.14% | Credit market proxy |
| HY OAS | 3.02% | 36.0 bp | 39.0 bp | 30.0 bp | Credit spread stress |
| IG OAS | 0.83% | 6.0 bp | 3.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -4.70 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 0.69 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 9.3% | High-rate absorption |
| R1 | 78.5% | Bear steepening + dollar pressure |
| R2 | 6.8% | Credit / sovereign stress spillover |
| R3 | 5.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: no strong evidence
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

