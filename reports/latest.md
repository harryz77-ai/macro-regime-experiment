# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-09T10:51:54.308531+00:00
- Latest market date: 2026-06-09
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **62.0%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.76 | 0.55% | 1.86% | -0.59% | Dollar pressure |
| SPY | 739.22 | -2.55% | 0.22% | 11.29% | Broad risk asset |
| QQQ | 716.07 | -3.59% | 0.68% | 20.04% | High-duration growth |
| IWM | 284.11 | -1.69% | -0.02% | 15.04% | Small-cap financing sensitivity |
| TLT | 84.62 | -0.99% | -1.31% | -1.57% | Long-duration bond stress |
| EEM | 65.75 | -6.18% | -3.22% | 15.45% | EM dollar/rate transmission |
| HYG | 79.54 | -0.38% | -0.24% | 1.77% | Credit market proxy |
| HY OAS | 2.76% | 2.0 bp | -3.0 bp | -51.0 bp | Credit spread stress |
| IG OAS | 0.74% | 0.0 bp | -4.0 bp | -20.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.24 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.44 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.2% | High-rate absorption |
| R1 | 62.0% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit
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

