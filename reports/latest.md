# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-01T01:02:23.816934+00:00
- Latest market date: 2026-07-31
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **65.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.680% | -3.0 bp | 20.0 bp | 23.0 bp | Long-end rate pressure |
| US 30Y yield | 5.210% | 4.0 bp | 24.0 bp | 19.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.80 | -1.64% | -1.05% | 1.34% | Dollar pressure |
| SPY | 747.03 | 1.10% | 0.30% | 3.48% | Broad risk asset |
| QQQ | 687.99 | 0.55% | -3.45% | 1.05% | High-duration growth |
| IWM | 291.20 | 0.01% | -2.14% | 3.30% | Small-cap financing sensitivity |
| TLT | 82.25 | -1.20% | -3.81% | -2.99% | Long-duration bond stress |
| EEM | 64.09 | 1.20% | -2.45% | -1.49% | EM dollar/rate transmission |
| HYG | 79.48 | 0.32% | -0.29% | 0.42% | Credit market proxy |
| HY OAS | 2.84% | 7.0 bp | 9.0 bp | 3.0 bp | Credit spread stress |
| IG OAS | 0.80% | 1.0 bp | 5.0 bp | 1.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.45 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.75 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 19.0% | High-rate absorption |
| R1 | 65.7% | Bear steepening + dollar pressure |
| R2 | 8.4% | Credit / sovereign stress spillover |
| R3 | 7.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

