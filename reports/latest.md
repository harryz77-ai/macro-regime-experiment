# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-27T02:17:40.332066+00:00
- Latest market date: 2026-10-26
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **43.8%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.000% | -9.0 bp | -18.0 bp | 33.0 bp | Long-end rate pressure |
| US 30Y yield | 5.330% | -10.0 bp | -14.0 bp | 13.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.04 | 0.06% | 0.83% | 2.24% | Dollar pressure |
| SPY | 765.37 | -0.14% | -0.03% | 2.71% | Broad risk asset |
| QQQ | 712.20 | -0.86% | -3.30% | 3.63% | High-duration growth |
| IWM | 276.99 | 2.10% | -1.08% | -4.63% | Small-cap financing sensitivity |
| TLT | 81.68 | 2.79% | 4.31% | 0.49% | Long-duration bond stress |
| EEM | 61.82 | -2.35% | -8.01% | -3.54% | EM dollar/rate transmission |
| HYG | 77.20 | 0.48% | 0.00% | -1.43% | Credit market proxy |
| HY OAS | 3.38% | 7.0 bp | 45.0 bp | 53.0 bp | Credit spread stress |
| IG OAS | 0.91% | 6.0 bp | 10.0 bp | 12.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.05 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.97 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 43.8% | High-rate absorption |
| R1 | 33.3% | Bear steepening + dollar pressure |
| R2 | 7.0% | Credit / sovereign stress spillover |
| R3 | 15.9% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: TLT rallied over 20D

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 55.0% | High-rate absorption |
| R1 | 25.0% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
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

