# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-10-23T01:44:41.372446+00:00
- Latest market date: 2026-10-22
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **43.8%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.130% | -6.0 bp | 17.0 bp | 48.0 bp | Long-end rate pressure |
| US 30Y yield | 5.420% | -10.0 bp | 13.0 bp | 30.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.57 | -0.42% | 0.28% | 0.76% | Dollar pressure |
| SPY | 763.96 | -1.01% | -0.42% | 4.99% | Broad risk asset |
| QQQ | 704.47 | -3.23% | -4.94% | 6.57% | High-duration growth |
| IWM | 276.67 | 0.58% | -1.77% | -3.87% | Small-cap financing sensitivity |
| TLT | 81.74 | 2.21% | 3.34% | -0.16% | Long-duration bond stress |
| EEM | 61.72 | -3.50% | -8.22% | 1.06% | EM dollar/rate transmission |
| HYG | 77.10 | -0.04% | -0.57% | -1.26% | Credit market proxy |
| HY OAS | 3.27% | 2.0 bp | 54.0 bp | 40.0 bp | Credit spread stress |
| IG OAS | 0.88% | 4.0 bp | 11.0 bp | 7.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.35 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.80 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 43.8% | High-rate absorption |
| R1 | 30.8% | Bear steepening + dollar pressure |
| R2 | 13.4% | Credit / sovereign stress spillover |
| R3 | 12.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; DXY is stable
- **R1**: EEM underperformed SPY over 20D
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

