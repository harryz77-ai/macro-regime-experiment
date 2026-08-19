# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-08-19T23:46:31.419559+00:00
- Latest market date: 2026-08-19
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **50.2%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.710% | 1.0 bp | 8.0 bp | 14.0 bp | Long-end rate pressure |
| US 30Y yield | 5.280% | 4.0 bp | 15.0 bp | 18.0 bp | Term premium / fiscal supply pressure |
| DXY | 98.77 | -1.24% | -1.97% | -0.54% | Dollar pressure |
| SPY | 769.06 | -0.44% | 2.90% | 3.41% | Broad risk asset |
| QQQ | 716.08 | -1.05% | 1.52% | -0.09% | High-duration growth |
| IWM | 301.72 | -0.33% | 2.70% | 6.07% | Small-cap financing sensitivity |
| TLT | 83.02 | 1.11% | -0.10% | -0.81% | Long-duration bond stress |
| EEM | 66.11 | -0.53% | 1.18% | 0.64% | EM dollar/rate transmission |
| HYG | 79.71 | 0.13% | 0.52% | 1.28% | Credit market proxy |
| HY OAS | 2.75% | 3.0 bp | 6.0 bp | 4.0 bp | Credit spread stress |
| IG OAS | 0.82% | 3.0 bp | 4.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.20 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.72 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 50.2% | High-rate absorption |
| R1 | 22.7% | Bear steepening + dollar pressure |
| R2 | 8.3% | Credit / sovereign stress spillover |
| R3 | 18.8% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: DXY weakened over 20D

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

