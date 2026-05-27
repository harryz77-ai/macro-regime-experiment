# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-05-27T12:02:47.334070+00:00
- Latest market date: 2026-05-27
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **39.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.560% | -3.0 bp | 25.0 bp | 59.0 bp | Long-end rate pressure |
| US 30Y yield | 5.070% | -5.0 bp | 16.0 bp | 43.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.14 | -0.16% | 0.53% | 0.77% | Dollar pressure |
| SPY | 750.59 | 1.62% | 4.95% | 9.72% | Broad risk asset |
| QQQ | 730.28 | 3.46% | 9.94% | 20.40% | High-duration growth |
| IWM | 290.51 | 5.27% | 4.82% | 11.33% | Small-cap financing sensitivity |
| TLT | 85.10 | 1.84% | -1.00% | -5.26% | Long-duration bond stress |
| EEM | 68.40 | 5.28% | 7.48% | 9.30% | EM dollar/rate transmission |
| HYG | 80.18 | 0.80% | 0.11% | 0.83% | Credit market proxy |
| HY OAS | 2.74% | -9.0 bp | -10.0 bp | -29.0 bp | Credit spread stress |
| IG OAS | 0.74% | -1.0 bp | -7.0 bp | -11.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.13 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.53 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 33.3% | High-rate absorption |
| R1 | 39.6% | Bear steepening + dollar pressure |
| R2 | 11.2% | Credit / sovereign stress spillover |
| R3 | 15.9% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; credit spread pressure is not yet disorderly
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

