# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-18T00:55:11.405973+00:00
- Latest market date: 2026-07-17
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **48.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.570% | 3.0 bp | 14.0 bp | 31.0 bp | Long-end rate pressure |
| US 30Y yield | 5.090% | 4.0 bp | 16.0 bp | 21.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.75 | -0.21% | 0.66% | 2.38% | Dollar pressure |
| SPY | 743.29 | -1.54% | 0.57% | 5.84% | Broad risk asset |
| QQQ | 695.33 | -4.16% | -3.66% | 8.03% | High-duration growth |
| IWM | 294.04 | -0.66% | 1.44% | 7.37% | Small-cap financing sensitivity |
| TLT | 84.52 | 0.06% | -1.74% | -1.26% | Long-duration bond stress |
| EEM | 63.29 | -5.40% | -7.69% | 2.20% | EM dollar/rate transmission |
| HYG | 79.65 | -0.08% | 0.36% | 0.60% | Credit market proxy |
| HY OAS | 2.71% | 1.0 bp | 5.0 bp | -15.0 bp | Credit spread stress |
| IG OAS | 0.78% | 2.0 bp | 4.0 bp | -2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.86 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -8.26 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 48.6% | High-rate absorption |
| R1 | 33.0% | Bear steepening + dollar pressure |
| R2 | 9.9% | Credit / sovereign stress spillover |
| R3 | 8.5% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

