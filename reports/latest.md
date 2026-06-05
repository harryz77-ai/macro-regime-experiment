# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-05T11:48:27.985669+00:00
- Latest market date: 2026-06-05
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **39.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.21 | 0.30% | 0.98% | -0.02% | Dollar pressure |
| SPY | 757.09 | 0.33% | 3.17% | 12.11% | Broad risk asset |
| QQQ | 740.61 | 0.68% | 6.44% | 22.01% | High-duration growth |
| IWM | 292.01 | -0.01% | 1.82% | 15.46% | Small-cap financing sensitivity |
| TLT | 85.50 | 0.11% | -0.28% | -2.02% | Long-duration bond stress |
| EEM | 69.10 | 0.71% | 2.39% | 17.76% | EM dollar/rate transmission |
| HYG | 79.83 | 0.01% | 0.10% | 1.26% | Credit market proxy |
| HY OAS | 2.75% | 3.0 bp | -4.0 bp | -42.0 bp | Credit spread stress |
| IG OAS | 0.74% | 1.0 bp | -5.0 bp | -17.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.35 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.78 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 39.7% | High-rate absorption |
| R1 | 29.0% | Bear steepening + dollar pressure |
| R2 | 12.5% | Credit / sovereign stress spillover |
| R3 | 18.8% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

