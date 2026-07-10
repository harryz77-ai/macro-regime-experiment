# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-10T01:08:25.582280+00:00
- Latest market date: 2026-07-09
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
| US 10Y yield | 4.560% | 12.0 bp | 0.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.060% | 15.0 bp | 3.0 bp | 15.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.81 | -0.57% | 0.90% | 2.48% | Dollar pressure |
| SPY | 751.71 | 0.80% | 2.25% | 9.85% | Broad risk asset |
| QQQ | 723.28 | -0.26% | 2.30% | 17.28% | High-duration growth |
| IWM | 297.24 | -0.69% | 4.54% | 12.40% | Small-cap financing sensitivity |
| TLT | 84.49 | -1.20% | -0.37% | -1.88% | Long-duration bond stress |
| EEM | 66.78 | 0.45% | 1.99% | 9.92% | EM dollar/rate transmission |
| HYG | 79.75 | 0.20% | 0.63% | 0.35% | Credit market proxy |
| HY OAS | 2.70% | -4.0 bp | -10.0 bp | -16.0 bp | Credit spread stress |
| IG OAS | 0.76% | 0.0 bp | 1.0 bp | -5.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.28 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.27 pp | n/a | EM relative stress |

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

