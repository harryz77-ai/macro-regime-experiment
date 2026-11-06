# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-06T03:31:28.811299+00:00
- Latest market date: 2026-11-05
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
| US 10Y yield | 4.900% | -15.0 bp | -37.0 bp | 18.0 bp | Long-end rate pressure |
| US 30Y yield | 5.280% | -9.0 bp | -36.0 bp | 3.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.70 | -0.33% | -0.43% | 1.69% | Dollar pressure |
| SPY | 733.00 | -4.73% | -5.29% | -4.88% | Broad risk asset |
| QQQ | 647.05 | -9.55% | -13.45% | -10.50% | High-duration growth |
| IWM | 270.98 | -4.59% | -2.37% | -10.25% | Small-cap financing sensitivity |
| TLT | 81.93 | 0.54% | 5.21% | 0.16% | Long-duration bond stress |
| EEM | 58.05 | -7.45% | -12.18% | -12.65% | EM dollar/rate transmission |
| HYG | 77.28 | -0.39% | 0.18% | -2.39% | Credit market proxy |
| HY OAS | 3.32% | 18.0 bp | 23.0 bp | 61.0 bp | Credit spread stress |
| IG OAS | 0.91% | 5.0 bp | 9.0 bp | 12.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.91 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.89 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 19.8% | High-rate absorption |
| R1 | 39.6% | Bear steepening + dollar pressure |
| R2 | 11.2% | Credit / sovereign stress spillover |
| R3 | 29.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D; TLT rallied over 20D

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 25.0% | High-rate absorption |
| R1 | 43.0% | Bear steepening + dollar pressure |
| R2 | 18.0% | Credit / sovereign stress spillover |
| R3 | 14.0% | Rate decline / policy repair |

## 7. Risk Alerts

- R1 continuation: **ON**
- R2 upgrade warning: **ON**
- R3 policy-repair signal: **ON**

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

