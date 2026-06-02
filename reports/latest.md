# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-02T12:56:10.683567+00:00
- Latest market date: 2026-06-02
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
| US 10Y yield | 4.450% | -12.0 bp | 5.0 bp | 32.0 bp | Long-end rate pressure |
| US 30Y yield | 4.990% | -11.0 bp | 1.0 bp | 25.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.08 | -0.09% | 0.62% | 0.09% | Dollar pressure |
| SPY | 758.54 | 1.73% | 5.26% | 11.64% | Broad risk asset |
| QQQ | 742.74 | 3.51% | 10.17% | 22.13% | High-duration growth |
| IWM | 288.98 | 1.35% | 3.47% | 12.75% | Small-cap financing sensitivity |
| TLT | 85.47 | 1.33% | 0.23% | -2.62% | Long-duration bond stress |
| EEM | 70.08 | 6.38% | 9.28% | 21.60% | EM dollar/rate transmission |
| HYG | 79.84 | 0.42% | 0.24% | 1.22% | Credit market proxy |
| HY OAS | 2.74% | 0.0 bp | -4.0 bp | -45.0 bp | Credit spread stress |
| IG OAS | 0.74% | 0.0 bp | -6.0 bp | -11.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.78 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 4.02 pp | n/a | EM relative stress |

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

