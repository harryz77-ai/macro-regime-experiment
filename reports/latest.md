# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-28T04:52:22.125997+00:00
- Latest market date: 2026-11-27
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
| US 10Y yield | 4.850% | -22.0 bp | -14.0 bp | 12.0 bp | Long-end rate pressure |
| US 30Y yield | 5.240% | -17.0 bp | -6.0 bp | 2.0 bp | Term premium / fiscal supply pressure |
| DXY | 104.01 | 0.11% | 1.93% | 4.47% | Dollar pressure |
| SPY | 728.32 | 1.74% | -5.33% | -4.58% | Broad risk asset |
| QQQ | 650.99 | 0.92% | -9.00% | -8.12% | High-duration growth |
| IWM | 273.79 | 3.62% | -3.60% | -6.63% | Small-cap financing sensitivity |
| TLT | 81.27 | 1.14% | 0.15% | -0.01% | Long-duration bond stress |
| EEM | 58.10 | 2.38% | -7.37% | -13.48% | EM dollar/rate transmission |
| HYG | 76.61 | 0.10% | -0.74% | -2.22% | Credit market proxy |
| HY OAS | 3.77% | 25.0 bp | 51.0 bp | 112.0 bp | Credit spread stress |
| IG OAS | 0.99% | 5.0 bp | 10.0 bp | 18.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.74 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.03 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 24.5% | High-rate absorption |
| R1 | 50.1% | Bear steepening + dollar pressure |
| R2 | 13.4% | Credit / sovereign stress spillover |
| R3 | 12.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D
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

