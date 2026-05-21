# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-05-21T11:53:02.158419+00:00
- Latest market date: 2026-05-21
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **63.8%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.670% | 21.0 bp | 37.0 bp | 63.0 bp | Long-end rate pressure |
| US 30Y yield | 5.180% | 15.0 bp | 29.0 bp | 48.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.25 | 0.37% | 0.46% | 1.59% | Dollar pressure |
| SPY | 741.25 | -0.14% | 4.22% | 8.14% | Broad risk asset |
| QQQ | 713.15 | -0.22% | 8.86% | 17.47% | High-duration growth |
| IWM | 279.87 | -0.99% | 1.23% | 6.47% | Small-cap financing sensitivity |
| TLT | 83.91 | -1.05% | -2.91% | -5.63% | Long-duration bond stress |
| EEM | 65.46 | -2.60% | 3.28% | 4.54% | EM dollar/rate transmission |
| HYG | 79.86 | -0.06% | -0.28% | 0.31% | Credit market proxy |
| HY OAS | 2.86% | 4.0 bp | 1.0 bp | -8.0 bp | Credit spread stress |
| IG OAS | 0.76% | -1.0 bp | -4.0 bp | -4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.00 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.94 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.6% | High-rate absorption |
| R1 | 63.8% | Bear steepening + dollar pressure |
| R2 | 8.3% | Credit / sovereign stress spillover |
| R3 | 9.3% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

