# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-18T02:01:20.833835+00:00
- Latest market date: 2026-06-17
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
| US 10Y yield | 4.430% | -10.0 bp | -18.0 bp | 9.0 bp | Long-end rate pressure |
| US 30Y yield | 4.930% | -8.0 bp | -21.0 bp | 2.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.27 | 0.32% | 0.98% | 1.34% | Dollar pressure |
| SPY | 740.96 | 2.14% | 0.99% | 13.06% | Broad risk asset |
| QQQ | 722.51 | 4.15% | 2.99% | 22.88% | High-duration growth |
| IWM | 289.88 | 3.02% | 6.44% | 17.43% | Small-cap financing sensitivity |
| TLT | 86.33 | 1.71% | 4.40% | 1.10% | Long-duration bond stress |
| EEM | 68.56 | 6.58% | 7.25% | 20.25% | EM dollar/rate transmission |
| HYG | 79.73 | 0.33% | 0.99% | 1.90% | Credit market proxy |
| HY OAS | 2.71% | -7.0 bp | -9.0 bp | -46.0 bp | Credit spread stress |
| IG OAS | 0.75% | 0.0 bp | 0.0 bp | -12.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.45 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 6.26 pp | n/a | EM relative stress |

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
- **R3**: TLT rallied over 20D

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

