# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-23T01:38:30.272468+00:00
- Latest market date: 2026-09-22
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
| US 10Y yield | 4.960% | -1.0 bp | 22.0 bp | 56.0 bp | Long-end rate pressure |
| US 30Y yield | 5.290% | -5.0 bp | 2.0 bp | 43.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.64 | 1.00% | 1.66% | -0.71% | Dollar pressure |
| SPY | 773.50 | 1.91% | 1.27% | 5.60% | Broad risk asset |
| QQQ | 741.47 | 4.66% | 4.04% | 3.61% | High-duration growth |
| IWM | 285.58 | -0.55% | -4.55% | -4.21% | Small-cap financing sensitivity |
| TLT | 81.80 | 1.08% | 0.08% | -5.27% | Long-duration bond stress |
| EEM | 68.83 | 4.30% | 2.55% | 1.28% | EM dollar/rate transmission |
| HYG | 78.68 | 0.19% | -0.63% | -0.02% | Credit market proxy |
| HY OAS | 2.66% | -5.0 bp | -3.0 bp | -14.0 bp | Credit spread stress |
| IG OAS | 0.77% | -3.0 bp | -4.0 bp | 1.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -5.81 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.28 pp | n/a | EM relative stress |

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

