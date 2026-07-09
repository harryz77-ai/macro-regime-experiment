# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-09T01:10:00.173411+00:00
- Latest market date: 2026-07-08
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **55.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.550% | 17.0 bp | 0.0 bp | 26.0 bp | Long-end rate pressure |
| US 30Y yield | 5.050% | 19.0 bp | 4.0 bp | 15.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.99 | -0.20% | 0.93% | 2.37% | Dollar pressure |
| SPY | 745.40 | -0.18% | 1.10% | 9.99% | Broad risk asset |
| QQQ | 711.44 | -3.39% | -0.54% | 16.55% | High-duration growth |
| IWM | 293.48 | -2.32% | 3.54% | 12.58% | Small-cap financing sensitivity |
| TLT | 84.36 | -2.02% | 0.06% | -1.74% | Long-duration bond stress |
| EEM | 66.23 | -3.19% | 1.25% | 9.93% | EM dollar/rate transmission |
| HYG | 79.66 | 0.07% | 0.62% | 0.61% | Credit market proxy |
| HY OAS | 2.67% | -8.0 bp | -11.0 bp | -18.0 bp | Credit spread stress |
| IG OAS | 0.76% | 0.0 bp | 1.0 bp | -4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.45 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 0.16 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 55.7% | High-rate absorption |
| R1 | 24.5% | Bear steepening + dollar pressure |
| R2 | 10.6% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

