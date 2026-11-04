# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-04T03:06:10.483957+00:00
- Latest market date: 2026-11-03
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
| US 10Y yield | 4.910% | -9.0 bp | -37.0 bp | 22.0 bp | Long-end rate pressure |
| US 30Y yield | 5.280% | -3.0 bp | -35.0 bp | 6.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.32 | -0.98% | -0.51% | 1.51% | Dollar pressure |
| SPY | 754.35 | -1.99% | -3.18% | -2.17% | Broad risk asset |
| QQQ | 685.28 | -4.99% | -9.79% | -4.84% | High-duration growth |
| IWM | 279.79 | -0.14% | -0.55% | -6.49% | Small-cap financing sensitivity |
| TLT | 81.11 | -0.64% | 4.96% | -0.78% | Long-duration bond stress |
| EEM | 61.10 | -2.27% | -10.50% | -6.25% | EM dollar/rate transmission |
| HYG | 76.98 | -0.80% | -0.38% | -2.61% | Credit market proxy |
| HY OAS | 3.43% | 13.0 bp | 31.0 bp | 73.0 bp | Credit spread stress |
| IG OAS | 0.94% | 4.0 bp | 10.0 bp | 16.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.62 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.33 pp | n/a | EM relative stress |

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

