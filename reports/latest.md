# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-20T04:09:12.957167+00:00
- Latest market date: 2026-11-19
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
| US 10Y yield | 5.070% | 9.0 bp | -5.0 bp | 33.0 bp | Long-end rate pressure |
| US 30Y yield | 5.410% | 6.0 bp | -1.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.83 | 0.64% | 2.18% | 4.70% | Dollar pressure |
| SPY | 715.87 | -5.45% | -6.29% | -6.32% | Broad risk asset |
| QQQ | 645.04 | -6.27% | -8.44% | -9.23% | High-duration growth |
| IWM | 264.22 | -5.11% | -4.50% | -11.38% | Small-cap financing sensitivity |
| TLT | 80.35 | 0.79% | -1.29% | -2.37% | Long-duration bond stress |
| EEM | 56.75 | -7.18% | -8.05% | -15.51% | EM dollar/rate transmission |
| HYG | 76.53 | -0.58% | -0.22% | -2.76% | Credit market proxy |
| HY OAS | 3.47% | 17.0 bp | 20.0 bp | 80.0 bp | Credit spread stress |
| IG OAS | 0.93% | 3.0 bp | 5.0 bp | 13.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.79 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.76 pp | n/a | EM relative stress |

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

