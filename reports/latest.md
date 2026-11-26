# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-11-26T05:17:30.129805+00:00
- Latest market date: 2026-11-26
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
| US 10Y yield | 4.910% | -19.0 bp | -9.0 bp | 24.0 bp | Long-end rate pressure |
| US 30Y yield | 5.300% | -16.0 bp | -1.0 bp | 11.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.82 | -0.08% | 1.74% | 4.28% | Dollar pressure |
| SPY | 716.70 | -1.85% | -7.20% | -5.68% | Broad risk asset |
| QQQ | 633.93 | -3.88% | -12.63% | -10.32% | High-duration growth |
| IWM | 268.87 | -0.46% | -4.42% | -7.23% | Small-cap financing sensitivity |
| TLT | 82.24 | 2.52% | 1.97% | 1.28% | Long-duration bond stress |
| EEM | 56.40 | -2.56% | -11.21% | -15.53% | EM dollar/rate transmission |
| HYG | 76.52 | -0.17% | -0.87% | -2.33% | Credit market proxy |
| HY OAS | 3.72% | 29.0 bp | 54.0 bp | 107.0 bp | Credit spread stress |
| IG OAS | 0.98% | 6.0 bp | 10.0 bp | 17.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.79 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.01 pp | n/a | EM relative stress |

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

