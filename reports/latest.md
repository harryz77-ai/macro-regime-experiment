# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-03T02:12:53.555414+00:00
- Latest market date: 2026-10-02
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
| US 10Y yield | 5.240% | 6.0 bp | 45.0 bp | 68.0 bp | Long-end rate pressure |
| US 30Y yield | 5.610% | 14.0 bp | 34.0 bp | 55.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.92 | 0.94% | 2.95% | 0.97% | Dollar pressure |
| SPY | 769.64 | -0.22% | -0.21% | 2.64% | Broad risk asset |
| QQQ | 749.58 | 0.68% | 4.56% | 3.74% | High-duration growth |
| IWM | 281.52 | -0.16% | -4.38% | -5.04% | Small-cap financing sensitivity |
| TLT | 77.48 | -1.93% | -5.21% | -7.20% | Long-duration bond stress |
| EEM | 67.67 | -0.46% | 0.30% | 1.33% | EM dollar/rate transmission |
| HYG | 76.91 | -0.78% | -2.47% | -2.13% | Credit market proxy |
| HY OAS | 3.24% | 44.0 bp | 59.0 bp | 54.0 bp | Credit spread stress |
| IG OAS | 0.86% | 7.0 bp | 5.0 bp | 10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -4.17 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 0.51 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 9.9% | High-rate absorption |
| R1 | 76.7% | Bear steepening + dollar pressure |
| R2 | 7.4% | Credit / sovereign stress spillover |
| R3 | 6.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: no strong evidence
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; TLT sold off over 20D
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

- R1 continuation: **not confirmed**
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

