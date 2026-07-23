# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-23T01:00:36.758504+00:00
- Latest market date: 2026-07-22
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **49.0%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.630% | 5.0 bp | 12.0 bp | 29.0 bp | Long-end rate pressure |
| US 30Y yield | 5.130% | 5.0 bp | 18.0 bp | 21.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.11 | 0.60% | -0.30% | 2.64% | Dollar pressure |
| SPY | 747.41 | -0.98% | 1.89% | 4.96% | Broad risk asset |
| QQQ | 705.35 | -1.73% | -1.16% | 6.36% | High-duration growth |
| IWM | 293.79 | -0.67% | -0.52% | 6.45% | Small-cap financing sensitivity |
| TLT | 83.44 | -0.95% | -2.84% | -2.68% | Long-duration bond stress |
| EEM | 64.99 | -0.88% | -3.25% | 2.49% | EM dollar/rate transmission |
| HYG | 79.52 | -0.36% | 0.02% | 0.30% | Credit market proxy |
| HY OAS | 2.69% | -3.0 bp | -2.0 bp | -13.0 bp | Credit spread stress |
| IG OAS | 0.78% | -1.0 bp | 4.0 bp | -3.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.40 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -5.13 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 49.0% | High-rate absorption |
| R1 | 38.5% | Bear steepening + dollar pressure |
| R2 | 4.8% | Credit / sovereign stress spillover |
| R3 | 7.6% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

- R1 continuation: **ON**
- R2 upgrade warning: **ON**
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

