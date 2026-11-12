# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-12T04:01:02.448482+00:00
- Latest market date: 2026-11-11
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **46.0%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.880% | -3.0 bp | -36.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.260% | -2.0 bp | -34.0 bp | 5.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.01 | 1.48% | 0.45% | 3.38% | Dollar pressure |
| SPY | 759.81 | -0.91% | -1.27% | -0.75% | Broad risk asset |
| QQQ | 690.38 | -0.23% | -5.29% | -3.68% | High-duration growth |
| IWM | 283.09 | -0.33% | 4.32% | -5.46% | Small-cap financing sensitivity |
| TLT | 80.92 | -1.03% | 3.00% | 0.29% | Long-duration bond stress |
| EEM | 62.04 | 0.68% | -3.65% | -5.05% | EM dollar/rate transmission |
| HYG | 77.35 | -0.22% | 1.23% | -1.26% | Credit market proxy |
| HY OAS | 3.34% | -9.0 bp | 23.0 bp | 64.0 bp | Credit spread stress |
| IG OAS | 0.91% | -3.0 bp | 8.0 bp | 10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.59 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.38 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 22.7% | High-rate absorption |
| R1 | 46.0% | Bear steepening + dollar pressure |
| R2 | 12.5% | Credit / sovereign stress spillover |
| R3 | 18.8% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D

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

