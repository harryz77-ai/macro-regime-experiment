# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-05T00:54:00.454723+00:00
- Latest market date: 2026-08-04
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
| US 10Y yield | 4.700% | 5.0 bp | 22.0 bp | 34.0 bp | Long-end rate pressure |
| US 30Y yield | 5.230% | 11.0 bp | 24.0 bp | 29.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.84 | -1.52% | -1.28% | 1.62% | Dollar pressure |
| SPY | 771.33 | 4.11% | 3.16% | 5.71% | Broad risk asset |
| QQQ | 723.85 | 7.16% | 2.03% | 4.27% | High-duration growth |
| IWM | 301.71 | 2.84% | 1.86% | 7.14% | Small-cap financing sensitivity |
| TLT | 82.82 | -1.29% | -1.65% | -2.17% | Long-duration bond stress |
| EEM | 66.00 | 5.84% | 0.43% | -0.37% | EM dollar/rate transmission |
| HYG | 79.55 | 0.65% | 0.22% | 1.07% | Credit market proxy |
| HY OAS | 2.78% | -3.0 bp | 6.0 bp | -4.0 bp | Credit spread stress |
| IG OAS | 0.78% | -3.0 bp | 3.0 bp | 1.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.30 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.73 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 18.2% | High-rate absorption |
| R1 | 62.0% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: 10Y yield rose meaningfully over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

