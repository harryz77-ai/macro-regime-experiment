# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-28T02:30:10.124655+00:00
- Latest market date: 2026-10-27
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **52.2%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.000% | -15.0 bp | -17.0 bp | 32.0 bp | Long-end rate pressure |
| US 30Y yield | 5.310% | -17.0 bp | -18.0 bp | 10.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.40 | 0.66% | 1.02% | 2.44% | Dollar pressure |
| SPY | 769.66 | 0.08% | 0.71% | 1.83% | Broad risk asset |
| QQQ | 721.25 | 0.50% | -2.26% | 3.13% | High-duration growth |
| IWM | 280.18 | 1.60% | 0.42% | -5.17% | Small-cap financing sensitivity |
| TLT | 81.63 | 1.87% | 4.77% | 0.10% | Long-duration bond stress |
| EEM | 62.52 | -1.26% | -7.24% | -2.80% | EM dollar/rate transmission |
| HYG | 77.60 | 1.00% | 0.76% | -1.18% | Credit market proxy |
| HY OAS | 3.30% | 1.0 bp | 28.0 bp | 52.0 bp | Credit spread stress |
| IG OAS | 0.90% | 3.0 bp | 7.0 bp | 12.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.30 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.95 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 28.0% | High-rate absorption |
| R1 | 52.2% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
| R3 | 13.7% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: TLT rallied over 20D

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 55.0% | High-rate absorption |
| R1 | 25.0% | Bear steepening + dollar pressure |
| R2 | 6.0% | Credit / sovereign stress spillover |
| R3 | 14.0% | Rate decline / policy repair |

## 7. Risk Alerts

- R1 continuation: **ON**
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

