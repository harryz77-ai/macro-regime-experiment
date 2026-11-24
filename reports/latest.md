# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-24T07:01:08.336869+00:00
- Latest market date: 2026-11-24
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **50.1%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.920% | -23.0 bp | -4.0 bp | 28.0 bp | Long-end rate pressure |
| US 30Y yield | 5.310% | -16.0 bp | 2.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 104.33 | 0.81% | 1.97% | 4.93% | Dollar pressure |
| SPY | 722.29 | -2.39% | -5.63% | -5.88% | Broad risk asset |
| QQQ | 651.03 | -1.62% | -8.59% | -9.03% | High-duration growth |
| IWM | 265.74 | -2.64% | -4.06% | -9.91% | Small-cap financing sensitivity |
| TLT | 81.69 | 2.91% | 0.43% | -0.24% | Long-duration bond stress |
| EEM | 57.83 | -1.80% | -6.45% | -13.87% | EM dollar/rate transmission |
| HYG | 76.52 | -0.27% | -0.36% | -2.58% | Credit market proxy |
| HY OAS | 3.76% | 53.0 bp | 38.0 bp | 116.0 bp | Credit spread stress |
| IG OAS | 0.98% | 9.0 bp | 7.0 bp | 19.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.57 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.83 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 24.5% | High-rate absorption |
| R1 | 50.1% | Bear steepening + dollar pressure |
| R2 | 13.4% | Credit / sovereign stress spillover |
| R3 | 12.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

