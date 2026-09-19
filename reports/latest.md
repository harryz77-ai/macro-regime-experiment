# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-19T01:24:03.319888+00:00
- Latest market date: 2026-09-18
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **70.5%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.940% | -1.0 bp | 29.0 bp | 44.0 bp | Long-end rate pressure |
| US 30Y yield | 5.290% | -8.0 bp | 10.0 bp | 35.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.21 | 1.10% | 1.33% | -1.37% | Dollar pressure |
| SPY | 761.69 | -0.09% | 0.13% | 4.14% | Broad risk asset |
| QQQ | 721.45 | 0.92% | 1.48% | 1.52% | High-duration growth |
| IWM | 284.10 | -1.40% | -4.31% | -3.99% | Small-cap financing sensitivity |
| TLT | 81.25 | 0.47% | -0.95% | -5.94% | Long-duration bond stress |
| EEM | 67.03 | -1.19% | 0.62% | -0.33% | EM dollar/rate transmission |
| HYG | 78.53 | -0.09% | -0.75% | -0.17% | Credit market proxy |
| HY OAS | 2.70% | 0.0 bp | -5.0 bp | -8.0 bp | Credit spread stress |
| IG OAS | 0.78% | -2.0 bp | -4.0 bp | 2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -4.44 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 0.49 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 13.8% | High-rate absorption |
| R1 | 70.5% | Bear steepening + dollar pressure |
| R2 | 8.6% | Credit / sovereign stress spillover |
| R3 | 7.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: 10Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

