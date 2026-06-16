# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-16T18:13:34.926101+00:00
- Latest market date: 2026-06-16
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **55.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.480% | -7.0 bp | 1.0 bp | 23.0 bp | Long-end rate pressure |
| US 30Y yield | 4.970% | -4.0 bp | -5.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.51 | -0.40% | 0.55% | -0.14% | Dollar pressure |
| SPY | 752.18 | 2.05% | 1.83% | 15.98% | Broad risk asset |
| QQQ | 734.34 | 3.75% | 4.03% | 26.32% | High-duration growth |
| IWM | 293.70 | 3.29% | 6.68% | 21.54% | Small-cap financing sensitivity |
| TLT | 86.32 | 1.40% | 3.70% | 1.74% | Long-duration bond stress |
| EEM | 68.96 | 5.31% | 6.69% | 24.57% | EM dollar/rate transmission |
| HYG | 80.05 | 0.55% | 1.16% | 2.99% | Credit market proxy |
| HY OAS | 2.66% | -9.0 bp | -20.0 bp | -53.0 bp | Credit spread stress |
| IG OAS | 0.73% | -2.0 bp | -3.0 bp | -14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 4.85 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 4.85 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 55.7% | High-rate absorption |
| R1 | 24.5% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

