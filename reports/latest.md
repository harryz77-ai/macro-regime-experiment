# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-10T01:18:30.576032+00:00
- Latest market date: 2026-09-09
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **41.7%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.800% | 5.0 bp | 8.0 bp | 35.0 bp | Long-end rate pressure |
| US 30Y yield | 5.250% | 0.0 bp | 0.0 bp | 30.0 bp | Term premium / fiscal supply pressure |
| DXY | 98.78 | -0.89% | -1.04% | -0.97% | Dollar pressure |
| SPY | 765.96 | -0.14% | -0.91% | 4.09% | Broad risk asset |
| QQQ | 718.36 | 0.22% | -0.35% | 0.28% | High-duration growth |
| IWM | 294.67 | 0.25% | -1.77% | 1.71% | Small-cap financing sensitivity |
| TLT | 82.20 | -0.01% | 0.55% | -3.29% | Long-duration bond stress |
| EEM | 68.83 | 2.70% | 5.62% | 2.50% | EM dollar/rate transmission |
| HYG | 79.12 | -0.32% | 0.09% | 0.46% | Credit market proxy |
| HY OAS | 2.67% | 2.0 bp | -5.0 bp | -4.0 bp | Credit spread stress |
| IG OAS | 0.81% | 0.0 bp | 2.0 bp | 6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.86 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 6.53 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 41.7% | High-rate absorption |
| R1 | 31.2% | Bear steepening + dollar pressure |
| R2 | 12.2% | Credit / sovereign stress spillover |
| R3 | 15.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: credit spread pressure is not yet disorderly
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

