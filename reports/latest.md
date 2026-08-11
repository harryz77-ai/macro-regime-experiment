# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-11T00:00:28.865458+00:00
- Latest market date: 2026-08-10
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **46.3%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.650% | -10.0 bp | 9.0 bp | 19.0 bp | Long-end rate pressure |
| US 30Y yield | 5.190% | -8.0 bp | 13.0 bp | 16.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.79 | -0.17% | -1.47% | 1.33% | Dollar pressure |
| SPY | 773.03 | 2.03% | 3.18% | 4.41% | Broad risk asset |
| QQQ | 720.87 | 2.97% | 1.28% | 0.97% | High-duration growth |
| IWM | 299.98 | 1.27% | 2.21% | 6.38% | Small-cap financing sensitivity |
| TLT | 82.06 | -0.16% | -1.88% | -2.10% | Long-duration bond stress |
| EEM | 65.17 | 1.32% | 1.04% | -2.53% | EM dollar/rate transmission |
| HYG | 79.48 | 0.21% | 0.43% | 0.92% | Credit market proxy |
| HY OAS | 2.70% | -15.0 bp | 1.0 bp | -13.0 bp | Credit spread stress |
| IG OAS | 0.78% | -1.0 bp | 1.0 bp | 3.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.97 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.15 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 46.3% | High-rate absorption |
| R1 | 35.8% | Bear steepening + dollar pressure |
| R2 | 7.6% | Credit / sovereign stress spillover |
| R3 | 10.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

