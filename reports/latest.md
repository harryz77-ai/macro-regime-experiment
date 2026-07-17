# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-17T01:00:50.906370+00:00
- Latest market date: 2026-07-16
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **48.6%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.550% | -1.0 bp | 8.0 bp | 29.0 bp | Long-end rate pressure |
| US 30Y yield | 5.080% | 2.0 bp | 11.0 bp | 20.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.73 | -0.21% | 1.19% | 2.73% | Dollar pressure |
| SPY | 750.72 | -0.13% | 0.31% | 6.20% | Broad risk asset |
| QQQ | 705.94 | -2.40% | -3.17% | 9.27% | High-duration growth |
| IWM | 295.59 | -0.56% | 1.20% | 6.83% | Small-cap financing sensitivity |
| TLT | 84.21 | -0.33% | -1.94% | -2.16% | Long-duration bond stress |
| EEM | 64.19 | -3.88% | -6.48% | 2.13% | EM dollar/rate transmission |
| HYG | 79.80 | 0.06% | 0.17% | 0.52% | Credit market proxy |
| HY OAS | 2.71% | 1.0 bp | 8.0 bp | -15.0 bp | Credit spread stress |
| IG OAS | 0.79% | 3.0 bp | 5.0 bp | -1.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.89 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.79 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 37.2% | High-rate absorption |
| R1 | 48.6% | Bear steepening + dollar pressure |
| R2 | 5.7% | Credit / sovereign stress spillover |
| R3 | 8.5% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

