# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-24T01:25:30.240976+00:00
- Latest market date: 2026-06-23
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **43.8%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.510% | 3.0 bp | -6.0 bp | 9.0 bp | Long-end rate pressure |
| US 30Y yield | 4.950% | -2.0 bp | -15.0 bp | 2.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.42 | 1.80% | 2.11% | 1.52% | Dollar pressure |
| SPY | 733.58 | -2.56% | -1.36% | 14.01% | Broad risk asset |
| QQQ | 713.65 | -3.97% | -0.43% | 24.51% | High-duration growth |
| IWM | 295.32 | 0.23% | 3.82% | 19.63% | Small-cap financing sensitivity |
| TLT | 86.20 | 0.56% | 2.20% | 1.27% | Long-duration bond stress |
| EEM | 67.17 | -3.70% | 2.49% | 21.72% | EM dollar/rate transmission |
| HYG | 79.87 | -0.21% | 0.46% | 2.75% | Credit market proxy |
| HY OAS | 2.65% | -1.0 bp | -7.0 bp | -63.0 bp | Credit spread stress |
| IG OAS | 0.74% | 1.0 bp | 0.0 bp | -16.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.19 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 3.85 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 35.0% | High-rate absorption |
| R1 | 43.8% | Bear steepening + dollar pressure |
| R2 | 9.2% | Credit / sovereign stress spillover |
| R3 | 12.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

