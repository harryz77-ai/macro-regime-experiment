# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-09-12T01:22:17.380443+00:00
- Latest market date: 2026-09-11
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **55.7%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.950% | 16.0 bp | 27.0 bp | 48.0 bp | Long-end rate pressure |
| US 30Y yield | 5.370% | 10.0 bp | 13.0 bp | 40.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.10 | 0.10% | -0.87% | -0.45% | Dollar pressure |
| SPY | 757.83 | -0.96% | -1.90% | 0.66% | Broad risk asset |
| QQQ | 708.69 | -0.08% | -2.07% | -4.64% | High-duration growth |
| IWM | 287.70 | -2.15% | -4.96% | -2.36% | Small-cap financing sensitivity |
| TLT | 80.78 | -1.43% | -1.24% | -4.67% | Long-duration bond stress |
| EEM | 67.00 | -0.22% | 0.81% | -3.94% | EM dollar/rate transmission |
| HYG | 78.62 | -0.62% | -0.70% | -0.30% | Credit market proxy |
| HY OAS | 2.70% | 5.0 bp | -1.0 bp | 4.0 bp | Credit spread stress |
| IG OAS | 0.80% | -1.0 bp | 1.0 bp | 6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.06 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.71 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 28.7% | High-rate absorption |
| R1 | 55.7% | Bear steepening + dollar pressure |
| R2 | 6.4% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

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

