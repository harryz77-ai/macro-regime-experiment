# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-04T11:30:30.680431+00:00
- Latest market date: 2026-06-04
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **52.2%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.22 | 0.20% | 1.22% | 0.39% | Dollar pressure |
| SPY | 754.24 | 0.50% | 4.21% | 11.50% | Broad risk asset |
| QQQ | 744.21 | 2.02% | 9.18% | 22.61% | High-duration growth |
| IWM | 287.67 | -0.93% | 1.81% | 13.63% | Small-cap financing sensitivity |
| TLT | 85.31 | 0.41% | 0.25% | -3.28% | Long-duration bond stress |
| EEM | 69.92 | 2.24% | 6.91% | 19.62% | EM dollar/rate transmission |
| HYG | 79.68 | -0.05% | 0.21% | 0.91% | Credit market proxy |
| HY OAS | 2.71% | 0.0 bp | -4.0 bp | -38.0 bp | Credit spread stress |
| IG OAS | 0.74% | 0.0 bp | -4.0 bp | -14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.40 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.70 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 28.0% | High-rate absorption |
| R1 | 52.2% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
| R3 | 13.7% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: DXY strengthened over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

