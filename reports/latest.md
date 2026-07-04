# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-04T01:08:10.984019+00:00
- Latest market date: 2026-07-03
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
| US 10Y yield | 4.480% | 7.0 bp | 2.0 bp | 14.0 bp | Long-end rate pressure |
| US 30Y yield | 4.970% | 11.0 bp | 0.0 bp | 8.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.86 | -0.50% | 1.46% | 1.74% | Dollar pressure |
| SPY | 744.78 | 1.43% | -1.00% | 13.27% | Broad risk asset |
| QQQ | 712.60 | -0.53% | -4.14% | 21.20% | High-duration growth |
| IWM | 297.58 | -0.44% | 3.69% | 17.94% | Small-cap financing sensitivity |
| TLT | 85.51 | -1.74% | 0.60% | -0.57% | Long-duration bond stress |
| EEM | 65.70 | -3.33% | -5.55% | 15.24% | EM dollar/rate transmission |
| HYG | 79.71 | 0.25% | 0.50% | 0.98% | Credit market proxy |
| HY OAS | 2.75% | -3.0 bp | 1.0 bp | -19.0 bp | Credit spread stress |
| IG OAS | 0.75% | -1.0 bp | 1.0 bp | -7.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 4.69 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.55 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.2% | High-rate absorption |
| R1 | 62.0% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
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

- R1 continuation: **not confirmed**
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

