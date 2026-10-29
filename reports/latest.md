# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-29T02:38:32.495555+00:00
- Latest market date: 2026-10-28
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **39.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.990% | -13.0 bp | -25.0 bp | 24.0 bp | Long-end rate pressure |
| US 30Y yield | 5.300% | -12.0 bp | -26.0 bp | 3.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.09 | 0.31% | 0.63% | 2.20% | Dollar pressure |
| SPY | 772.31 | -0.10% | 1.27% | 0.38% | Broad risk asset |
| QQQ | 725.61 | 0.06% | -1.91% | 0.35% | High-duration growth |
| IWM | 281.29 | 1.74% | 1.22% | -6.52% | Small-cap financing sensitivity |
| TLT | 80.99 | 0.93% | 4.55% | -1.44% | Long-duration bond stress |
| EEM | 63.52 | -0.08% | -4.90% | -3.76% | EM dollar/rate transmission |
| HYG | 77.59 | 0.79% | 0.94% | -1.49% | Credit market proxy |
| HY OAS | 3.18% | -15.0 bp | 10.0 bp | 45.0 bp | Credit spread stress |
| IG OAS | 0.88% | 1.0 bp | 4.0 bp | 10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.05 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.17 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 33.3% | High-rate absorption |
| R1 | 39.6% | Bear steepening + dollar pressure |
| R2 | 11.2% | Credit / sovereign stress spillover |
| R3 | 15.9% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: TLT rallied over 20D

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

