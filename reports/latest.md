# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-22T01:41:36.440531+00:00
- Latest market date: 2026-10-21
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y, hy_oas, ig_oas
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **50.1%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 101.70 | -0.83% | 0.59% | 0.32% | Dollar pressure |
| SPY | 773.09 | 0.45% | 0.69% | 4.61% | Broad risk asset |
| QQQ | 725.20 | -0.51% | -2.16% | 7.47% | High-duration growth |
| IWM | 276.48 | 1.88% | -1.93% | -5.51% | Small-cap financing sensitivity |
| TLT | 80.24 | 1.71% | 0.13% | -3.61% | Long-duration bond stress |
| EEM | 63.57 | -1.27% | -6.11% | 1.94% | EM dollar/rate transmission |
| HYG | 76.98 | 0.22% | -1.00% | -1.63% | Credit market proxy |
| HY OAS | missing | missing | missing | missing | Credit spread stress |
| IG OAS | missing | missing | missing | missing | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.62 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.80 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 24.5% | High-rate absorption |
| R1 | 50.1% | Bear steepening + dollar pressure |
| R2 | 13.4% | Credit / sovereign stress spillover |
| R3 | 12.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: IWM underperformed SPY over 20D; EEM underperformed SPY over 20D
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

