# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-17T02:01:24.356396+00:00
- Latest market date: 2026-06-16
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **66.2%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.470% | -9.0 bp | -12.0 bp | 8.0 bp | Long-end rate pressure |
| US 30Y yield | 4.970% | -6.0 bp | -15.0 bp | 1.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.52 | -0.39% | 0.56% | -0.13% | Dollar pressure |
| SPY | 750.33 | 1.80% | 1.58% | 15.69% | Broad risk asset |
| QQQ | 729.86 | 3.11% | 3.40% | 25.55% | High-duration growth |
| IWM | 292.08 | 2.72% | 6.09% | 20.87% | Small-cap financing sensitivity |
| TLT | 86.19 | 1.26% | 3.55% | 1.59% | Long-duration bond stress |
| EEM | 68.64 | 4.83% | 6.20% | 24.01% | EM dollar/rate transmission |
| HYG | 80.03 | 0.51% | 1.13% | 2.96% | Credit market proxy |
| HY OAS | 2.66% | -9.0 bp | -20.0 bp | -53.0 bp | Credit spread stress |
| IG OAS | 0.73% | -2.0 bp | -3.0 bp | -14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 4.51 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 4.62 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 66.2% | High-rate absorption |
| R1 | 18.2% | Bear steepening + dollar pressure |
| R2 | 6.4% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

