# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-03T16:10:12.955637+00:00
- Latest market date: 2026-06-03
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **43.8%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.46 | 0.26% | 1.00% | 0.29% | Dollar pressure |
| SPY | 755.15 | 0.62% | 4.34% | 11.64% | Broad risk asset |
| QQQ | 743.52 | 1.93% | 9.08% | 22.49% | High-duration growth |
| IWM | 288.11 | -0.78% | 1.96% | 13.80% | Small-cap financing sensitivity |
| TLT | 85.15 | 0.22% | 0.07% | -3.45% | Long-duration bond stress |
| EEM | 69.82 | 2.10% | 6.77% | 19.46% | EM dollar/rate transmission |
| HYG | 79.68 | -0.06% | 0.20% | 0.90% | Credit market proxy |
| HY OAS | 2.71% | 0.0 bp | -4.0 bp | -38.0 bp | Credit spread stress |
| IG OAS | 0.74% | 0.0 bp | -4.0 bp | -14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.37 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.43 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 43.8% | High-rate absorption |
| R1 | 33.3% | Bear steepening + dollar pressure |
| R2 | 7.0% | Credit / sovereign stress spillover |
| R3 | 15.9% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

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

