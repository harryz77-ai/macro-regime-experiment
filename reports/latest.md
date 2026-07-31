# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-31T01:04:18.001192+00:00
- Latest market date: 2026-07-30
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **76.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.670% | 0.0 bp | 23.0 bp | 28.0 bp | Long-end rate pressure |
| US 30Y yield | 5.200% | 5.0 bp | 29.0 bp | 23.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.12 | -1.29% | -1.25% | 1.68% | Dollar pressure |
| SPY | 741.69 | 0.48% | -0.55% | 3.56% | Broad risk asset |
| QQQ | 683.55 | -1.22% | -5.74% | 1.70% | High-duration growth |
| IWM | 292.59 | 0.17% | -2.25% | 5.54% | Small-cap financing sensitivity |
| TLT | 82.80 | -0.44% | -3.18% | -1.80% | Long-duration bond stress |
| EEM | 63.59 | -1.56% | -4.35% | -0.28% | EM dollar/rate transmission |
| HYG | 79.47 | 0.30% | -0.15% | 0.56% | Credit market proxy |
| HY OAS | 2.87% | 19.0 bp | 13.0 bp | 8.0 bp | Credit spread stress |
| IG OAS | 0.81% | 3.0 bp | 5.0 bp | 2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.70 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.80 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 9.9% | High-rate absorption |
| R1 | 76.7% | Bear steepening + dollar pressure |
| R2 | 7.4% | Credit / sovereign stress spillover |
| R3 | 6.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: no strong evidence
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

