# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-24T00:55:32.124962+00:00
- Latest market date: 2026-07-23
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **51.2%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.670% | 12.0 bp | 17.0 bp | 36.0 bp | Long-end rate pressure |
| US 30Y yield | 5.150% | 7.0 bp | 21.0 bp | 24.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.45 | 0.71% | -0.16% | 3.01% | Dollar pressure |
| SPY | 738.18 | -1.67% | 0.67% | 3.48% | Broad risk asset |
| QQQ | 691.96 | -1.98% | -2.63% | 4.29% | High-duration growth |
| IWM | 292.09 | -1.18% | -1.55% | 5.65% | Small-cap financing sensitivity |
| TLT | 83.17 | -1.24% | -4.47% | -2.51% | Long-duration bond stress |
| EEM | 64.60 | 0.64% | -3.94% | 2.04% | EM dollar/rate transmission |
| HYG | 79.23 | -0.71% | -0.32% | -0.11% | Credit market proxy |
| HY OAS | 2.68% | -3.0 bp | -8.0 bp | -15.0 bp | Credit spread stress |
| IG OAS | 0.78% | -1.0 bp | 3.0 bp | -3.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.22 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.61 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 38.3% | High-rate absorption |
| R1 | 51.2% | Bear steepening + dollar pressure |
| R2 | 3.8% | Credit / sovereign stress spillover |
| R3 | 6.6% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 55.0% | High-rate absorption |
| R1 | 25.0% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
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

