# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-25T01:43:25.167998+00:00
- Latest market date: 2026-09-24
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **75.4%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.110% | 10.0 bp | 47.0 bp | 73.0 bp | Long-end rate pressure |
| US 30Y yield | 5.400% | 5.0 bp | 23.0 bp | 54.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.26 | 0.95% | 2.37% | 0.15% | Dollar pressure |
| SPY | 767.18 | 0.85% | 0.39% | 2.99% | Broad risk asset |
| QQQ | 741.10 | 3.48% | 4.29% | 0.74% | High-duration growth |
| IWM | 281.66 | -1.32% | -5.53% | -6.01% | Small-cap financing sensitivity |
| TLT | 79.42 | -2.89% | -4.29% | -7.03% | Long-duration bond stress |
| EEM | 67.25 | 2.33% | 0.00% | -0.27% | EM dollar/rate transmission |
| HYG | 77.89 | -0.68% | -2.01% | -1.18% | Credit market proxy |
| HY OAS | 2.73% | 3.0 bp | 6.0 bp | -1.0 bp | Credit spread stress |
| IG OAS | 0.77% | -1.0 bp | -3.0 bp | 1.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -5.92 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.39 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 11.2% | High-rate absorption |
| R1 | 75.4% | Bear steepening + dollar pressure |
| R2 | 7.4% | Credit / sovereign stress spillover |
| R3 | 6.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: 10Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

