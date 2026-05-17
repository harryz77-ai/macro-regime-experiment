# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-05-17T12:03:43.863364+00:00
- Latest market date: 2026-05-15
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **63.8%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.470% | 6.0 bp | 15.0 bp | 39.0 bp | Long-end rate pressure |
| US 30Y yield | 5.020% | 5.0 bp | 9.0 bp | 32.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.27 | 1.46% | 1.19% | 1.37% | Dollar pressure |
| SPY | 739.17 | 0.21% | 4.09% | 8.28% | Broad risk asset |
| QQQ | 708.93 | -0.32% | 9.26% | 17.62% | High-duration growth |
| IWM | 277.60 | -2.31% | 0.66% | 5.10% | Small-cap financing sensitivity |
| TLT | 83.66 | -2.81% | -3.56% | -5.62% | Long-duration bond stress |
| EEM | 65.07 | -4.22% | 2.25% | 6.60% | EM dollar/rate transmission |
| HYG | 79.46 | -0.85% | -0.96% | -0.35% | Credit market proxy |
| HY OAS | 2.76% | -3.0 bp | -10.0 bp | -10.0 bp | Credit spread stress |
| IG OAS | 0.76% | -3.0 bp | -5.0 bp | -2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.43 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.84 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.6% | High-rate absorption |
| R1 | 63.8% | Bear steepening + dollar pressure |
| R2 | 8.3% | Credit / sovereign stress spillover |
| R3 | 9.3% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; IWM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 25.0% | High-rate absorption |
| R1 | 43.0% | Bear steepening + dollar pressure |
| R2 | 18.0% | Credit / sovereign stress spillover |
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

