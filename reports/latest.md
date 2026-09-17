# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-17T01:36:07.854950+00:00
- Latest market date: 2026-09-16
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
| US 10Y yield | 5.000% | 20.0 bp | 28.0 bp | 54.0 bp | Long-end rate pressure |
| US 30Y yield | 5.360% | 11.0 bp | 5.0 bp | 46.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.30 | 1.55% | 0.65% | -0.71% | Dollar pressure |
| SPY | 754.05 | -1.10% | -1.75% | 1.30% | Broad risk asset |
| QQQ | 704.72 | -1.62% | -1.78% | -4.50% | High-duration growth |
| IWM | 283.92 | -2.06% | -5.19% | -4.53% | Small-cap financing sensitivity |
| TLT | 80.88 | -1.04% | -0.58% | -4.96% | Long-duration bond stress |
| EEM | 65.72 | -4.03% | 0.58% | -7.71% | EM dollar/rate transmission |
| HYG | 78.42 | -0.71% | -0.86% | -0.43% | Credit market proxy |
| HY OAS | 2.76% | 9.0 bp | 1.0 bp | 5.0 bp | Credit spread stress |
| IG OAS | 0.80% | -1.0 bp | -2.0 bp | 6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.44 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.33 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.2% | High-rate absorption |
| R1 | 62.0% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

