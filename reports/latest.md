# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-13T03:30:34.719053+00:00
- Latest market date: 2026-11-12
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **66.1%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.980% | 3.0 bp | -23.0 bp | 30.0 bp | Long-end rate pressure |
| US 30Y yield | 5.350% | 3.0 bp | -21.0 bp | 10.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.16 | 1.59% | 1.14% | 4.38% | Dollar pressure |
| SPY | 757.12 | 3.29% | -1.90% | -1.31% | Broad risk asset |
| QQQ | 688.17 | 6.35% | -5.47% | -3.80% | High-duration growth |
| IWM | 278.44 | 2.75% | 1.22% | -7.47% | Small-cap financing sensitivity |
| TLT | 79.72 | -2.70% | 0.11% | -2.81% | Long-duration bond stress |
| EEM | 61.14 | 5.32% | -4.41% | -7.52% | EM dollar/rate transmission |
| HYG | 76.98 | -0.39% | 0.33% | -1.96% | Credit market proxy |
| HY OAS | 3.30% | -10.0 bp | 14.0 bp | 55.0 bp | Credit spread stress |
| IG OAS | 0.90% | -3.0 bp | 7.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.12 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.51 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 13.4% | High-rate absorption |
| R1 | 66.1% | Bear steepening + dollar pressure |
| R2 | 10.9% | Credit / sovereign stress spillover |
| R3 | 9.5% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: no strong evidence
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

