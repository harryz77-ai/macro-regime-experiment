# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-29T04:16:12.205092+00:00
- Latest market date: 2026-08-27
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **62.7%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.670% | -2.0 bp | -1.0 bp | 21.0 bp | Long-end rate pressure |
| US 30Y yield | 5.190% | -4.0 bp | -2.0 bp | 22.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.16 | 0.26% | -0.85% | -0.06% | Dollar pressure |
| SPY | 771.10 | 1.11% | 3.97% | 1.78% | Broad risk asset |
| QQQ | 721.11 | 1.43% | 5.49% | -3.25% | High-duration growth |
| IWM | 299.81 | 0.72% | 2.47% | 3.04% | Small-cap financing sensitivity |
| TLT | 83.13 | 0.96% | 0.80% | -2.19% | Long-duration bond stress |
| EEM | 67.61 | 1.49% | 6.32% | -4.01% | EM dollar/rate transmission |
| HYG | 79.87 | 0.39% | 0.99% | 0.91% | Credit market proxy |
| HY OAS | 2.63% | -12.0 bp | -21.0 bp | -11.0 bp | Credit spread stress |
| IG OAS | 0.79% | -3.0 bp | -1.0 bp | 5.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.50 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.36 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 62.7% | High-rate absorption |
| R1 | 17.5% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
| R3 | 13.7% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

