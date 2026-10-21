# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-21T01:50:13.292046+00:00
- Latest market date: 2026-10-20
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **62.0%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.150% | -9.0 bp | 14.0 bp | 44.0 bp | Long-end rate pressure |
| US 30Y yield | 5.480% | -12.0 bp | 14.0 bp | 31.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.79 | -0.38% | 1.18% | 0.27% | Dollar pressure |
| SPY | 769.05 | -1.15% | -0.56% | 4.31% | Broad risk asset |
| QQQ | 717.63 | -3.49% | -3.99% | 5.32% | High-duration growth |
| IWM | 275.78 | -0.33% | -3.98% | -5.60% | Small-cap financing sensitivity |
| TLT | 80.13 | 2.25% | -1.59% | -3.18% | Long-duration bond stress |
| EEM | 63.32 | -3.68% | -8.36% | -0.47% | EM dollar/rate transmission |
| HYG | 76.83 | -0.34% | -1.90% | -1.64% | Credit market proxy |
| HY OAS | 3.29% | 18.0 bp | 63.0 bp | 48.0 bp | Credit spread stress |
| IG OAS | 0.87% | 4.0 bp | 10.0 bp | 6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.42 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.80 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.2% | High-rate absorption |
| R1 | 62.0% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; IWM underperformed SPY over 20D; EEM underperformed SPY over 20D
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

