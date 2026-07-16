# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-16T00:55:50.839984+00:00
- Latest market date: 2026-07-15
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **48.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.580% | 3.0 bp | 10.0 bp | 26.0 bp | Long-end rate pressure |
| US 30Y yield | 5.080% | 3.0 bp | 11.0 bp | 15.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.48 | -0.57% | 0.85% | 2.43% | Dollar pressure |
| SPY | 754.81 | 1.26% | 0.25% | 6.56% | Broad risk asset |
| QQQ | 717.74 | 0.89% | -3.42% | 10.74% | High-duration growth |
| IWM | 295.77 | 0.78% | 0.38% | 7.50% | Small-cap financing sensitivity |
| TLT | 84.24 | -0.14% | -1.36% | -2.15% | Long-duration bond stress |
| EEM | 65.57 | -1.00% | -5.99% | 3.57% | EM dollar/rate transmission |
| HYG | 79.81 | 0.19% | 0.17% | 0.45% | Credit market proxy |
| HY OAS | 2.72% | 5.0 bp | 1.0 bp | -12.0 bp | Credit spread stress |
| IG OAS | 0.79% | 3.0 bp | 4.0 bp | 0.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.13 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.25 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 48.6% | High-rate absorption |
| R1 | 33.0% | Bear steepening + dollar pressure |
| R2 | 9.9% | Credit / sovereign stress spillover |
| R3 | 8.5% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

