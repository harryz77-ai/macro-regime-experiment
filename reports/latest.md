# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-03T03:58:42.448970+00:00
- Latest market date: 2026-11-02
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
| US 10Y yield | 4.940% | -6.0 bp | -30.0 bp | 31.0 bp | Long-end rate pressure |
| US 30Y yield | 5.310% | -2.0 bp | -30.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.80 | -0.16% | -0.37% | 2.20% | Dollar pressure |
| SPY | 752.10 | -1.73% | -2.93% | -2.49% | Broad risk asset |
| QQQ | 681.09 | -4.37% | -9.93% | -5.70% | High-duration growth |
| IWM | 279.14 | 0.78% | -1.50% | -7.19% | Small-cap financing sensitivity |
| TLT | 81.73 | 0.06% | 5.99% | -0.47% | Long-duration bond stress |
| EEM | 61.11 | -1.15% | -11.09% | -6.90% | EM dollar/rate transmission |
| HYG | 76.89 | -0.40% | -0.12% | -2.46% | Credit market proxy |
| HY OAS | 3.44% | 6.0 bp | 34.0 bp | 74.0 bp | Credit spread stress |
| IG OAS | 0.94% | 3.0 bp | 9.0 bp | 16.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.44 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -8.15 pp | n/a | EM relative stress |

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

