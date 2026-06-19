# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-19T02:17:07.425077+00:00
- Latest market date: 2026-06-18
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **46.3%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.490% | -6.0 bp | -18.0 bp | 10.0 bp | Long-end rate pressure |
| US 30Y yield | 4.930% | -10.0 bp | -25.0 bp | -1.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.86 | 1.00% | 1.77% | 1.44% | Dollar pressure |
| SPY | 746.74 | 1.48% | 1.00% | 14.62% | Broad risk asset |
| QQQ | 740.62 | 3.28% | 3.85% | 26.82% | High-duration growth |
| IWM | 295.59 | 2.03% | 5.87% | 19.10% | Small-cap financing sensitivity |
| TLT | 86.75 | 0.90% | 3.79% | 2.04% | Long-duration bond stress |
| EEM | 70.79 | 5.42% | 8.70% | 25.90% | EM dollar/rate transmission |
| HYG | 80.01 | 0.09% | 0.70% | 2.61% | Credit market proxy |
| HY OAS | 2.63% | -17.0 bp | -15.0 bp | -58.0 bp | Credit spread stress |
| IG OAS | 0.74% | -1.0 bp | -1.0 bp | -14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 4.87 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 7.70 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 46.3% | High-rate absorption |
| R1 | 35.8% | Bear steepening + dollar pressure |
| R2 | 7.6% | Credit / sovereign stress spillover |
| R3 | 10.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

- R1 continuation: **not confirmed**
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

