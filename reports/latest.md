# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-07T01:51:14.636667+00:00
- Latest market date: 2026-08-06
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
| US 10Y yield | 4.630% | -4.0 bp | 7.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.170% | -3.0 bp | 11.0 bp | 22.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.94 | -0.07% | -0.99% | 2.04% | Dollar pressure |
| SPY | 768.56 | 3.62% | 2.24% | 4.23% | Broad risk asset |
| QQQ | 714.65 | 4.55% | -1.19% | 0.30% | High-duration growth |
| IWM | 298.25 | 1.93% | 0.34% | 4.78% | Small-cap financing sensitivity |
| TLT | 82.52 | 0.06% | -1.94% | -2.42% | Long-duration bond stress |
| EEM | 65.02 | 2.25% | -2.64% | -3.73% | EM dollar/rate transmission |
| HYG | 79.46 | 0.47% | 0.12% | 0.81% | Credit market proxy |
| HY OAS | 2.75% | -12.0 bp | 5.0 bp | -1.0 bp | Credit spread stress |
| IG OAS | 0.78% | -3.0 bp | 2.0 bp | 2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.90 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.88 pp | n/a | EM relative stress |

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

