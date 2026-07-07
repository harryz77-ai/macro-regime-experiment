# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-07T01:16:16.605316+00:00
- Latest market date: 2026-07-06
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **50.1%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.490% | 9.0 bp | 0.0 bp | 16.0 bp | Long-end rate pressure |
| US 30Y yield | 4.980% | 12.0 bp | -1.0 bp | 8.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.89 | -0.46% | 1.49% | 1.78% | Dollar pressure |
| SPY | 751.28 | 3.06% | -0.51% | 11.42% | Broad risk asset |
| QQQ | 722.82 | 2.31% | -2.29% | 19.39% | High-duration growth |
| IWM | 298.90 | -0.31% | 2.60% | 15.03% | Small-cap financing sensitivity |
| TLT | 85.45 | -1.83% | 0.31% | -0.96% | Long-duration bond stress |
| EEM | 67.57 | 0.57% | -1.71% | 12.38% | EM dollar/rate transmission |
| HYG | 79.87 | 0.51% | 0.51% | 0.59% | Credit market proxy |
| HY OAS | 2.74% | -9.0 bp | -2.0 bp | -21.0 bp | Credit spread stress |
| IG OAS | 0.75% | -2.0 bp | 1.0 bp | -7.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.11 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.19 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 24.5% | High-rate absorption |
| R1 | 50.1% | Bear steepening + dollar pressure |
| R2 | 13.4% | Credit / sovereign stress spillover |
| R3 | 12.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

