# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-07T03:01:20.539725+00:00
- Latest market date: 2026-11-06
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **39.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.840% | -14.0 bp | -44.0 bp | 14.0 bp | Long-end rate pressure |
| US 30Y yield | 5.250% | -7.0 bp | -42.0 bp | 1.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.28 | 0.39% | 0.07% | 2.32% | Dollar pressure |
| SPY | 735.29 | -2.70% | -5.56% | -5.24% | Broad risk asset |
| QQQ | 656.10 | -4.98% | -12.67% | -10.28% | High-duration growth |
| IWM | 273.67 | -2.03% | -1.89% | -9.59% | Small-cap financing sensitivity |
| TLT | 81.92 | 0.10% | 5.05% | -0.43% | Long-duration bond stress |
| EEM | 59.33 | -2.80% | -11.18% | -11.02% | EM dollar/rate transmission |
| HYG | 77.23 | -0.26% | 0.00% | -2.68% | Credit market proxy |
| HY OAS | 3.48% | 22.0 bp | 33.0 bp | 77.0 bp | Credit spread stress |
| IG OAS | 0.93% | 4.0 bp | 11.0 bp | 14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.67 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -5.62 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 19.8% | High-rate absorption |
| R1 | 39.6% | Bear steepening + dollar pressure |
| R2 | 11.2% | Credit / sovereign stress spillover |
| R3 | 29.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D; TLT rallied over 20D

## 6. Markov Prior

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 25.0% | High-rate absorption |
| R1 | 43.0% | Bear steepening + dollar pressure |
| R2 | 18.0% | Credit / sovereign stress spillover |
| R3 | 14.0% | Rate decline / policy repair |

## 7. Risk Alerts

- R1 continuation: **ON**
- R2 upgrade warning: **ON**
- R3 policy-repair signal: **ON**

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

