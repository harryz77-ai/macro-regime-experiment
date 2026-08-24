# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-24T23:46:10.649579+00:00
- Latest market date: 2026-08-24
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **43.8%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.740% | 6.0 bp | 5.0 bp | 26.0 bp | Long-end rate pressure |
| US 30Y yield | 5.270% | 2.0 bp | 11.0 bp | 26.0 bp | Term premium / fiscal supply pressure |
| DXY | 98.98 | -0.66% | -2.49% | -0.04% | Dollar pressure |
| SPY | 763.47 | -1.19% | 3.30% | 1.44% | Broad risk asset |
| QQQ | 706.32 | -3.23% | 3.55% | -3.87% | High-duration growth |
| IWM | 297.97 | -2.00% | 1.73% | 2.28% | Small-cap financing sensitivity |
| TLT | 82.56 | 1.49% | -1.02% | -2.58% | Long-duration bond stress |
| EEM | 66.11 | -1.80% | 3.91% | -3.14% | EM dollar/rate transmission |
| HYG | 79.70 | 0.11% | 1.03% | 0.80% | Credit market proxy |
| HY OAS | 2.70% | 3.0 bp | -9.0 bp | -4.0 bp | Credit spread stress |
| IG OAS | 0.81% | 1.0 bp | 1.0 bp | 7.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.57 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 0.62 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 43.8% | High-rate absorption |
| R1 | 19.8% | Bear steepening + dollar pressure |
| R2 | 7.0% | Credit / sovereign stress spillover |
| R3 | 29.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: DXY weakened over 20D; SPY and QQQ rallied over 20D

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

