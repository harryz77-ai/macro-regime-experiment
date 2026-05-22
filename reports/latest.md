# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-05-22T10:37:21.114924+00:00
- Latest market date: 2026-05-22
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **52.4%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.570% | 11.0 bp | 27.0 bp | 52.0 bp | Long-end rate pressure |
| US 30Y yield | 5.110% | 8.0 bp | 21.0 bp | 41.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.31 | 0.04% | 0.81% | 1.55% | Dollar pressure |
| SPY | 742.72 | -0.73% | 4.84% | 7.44% | Broad risk asset |
| QQQ | 714.51 | -0.73% | 9.69% | 16.01% | High-duration growth |
| IWM | 282.49 | -0.69% | 2.53% | 6.96% | Small-cap financing sensitivity |
| TLT | 84.22 | -0.82% | -2.33% | -5.29% | Long-duration bond stress |
| EEM | 66.03 | -2.00% | 5.90% | 4.30% | EM dollar/rate transmission |
| HYG | 79.90 | 0.06% | -0.06% | 0.23% | Credit market proxy |
| HY OAS | 2.80% | -2.0 bp | -4.0 bp | -18.0 bp | Credit spread stress |
| IG OAS | 0.75% | -1.0 bp | -4.0 bp | -7.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.31 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.06 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 25.5% | High-rate absorption |
| R1 | 52.4% | Bear steepening + dollar pressure |
| R2 | 9.7% | Credit / sovereign stress spillover |
| R3 | 12.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

