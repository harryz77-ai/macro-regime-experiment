# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-01T01:39:55.244126+00:00
- Latest market date: 2026-06-30
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
| US 10Y yield | 4.380% | -13.0 bp | -7.0 bp | 7.0 bp | Long-end rate pressure |
| US 30Y yield | 4.860% | -9.0 bp | -13.0 bp | -2.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.30 | -0.11% | 2.11% | 1.27% | Dollar pressure |
| SPY | 746.77 | 1.80% | -1.30% | 14.16% | Broad risk asset |
| QQQ | 736.40 | 3.19% | -0.74% | 26.02% | High-duration growth |
| IWM | 300.45 | 1.74% | 4.22% | 19.85% | Small-cap financing sensitivity |
| TLT | 86.42 | 0.26% | 1.11% | 0.33% | Long-duration bond stress |
| EEM | 68.41 | 1.85% | -1.88% | 21.52% | EM dollar/rate transmission |
| HYG | 79.97 | 0.13% | 0.16% | 1.56% | Credit market proxy |
| HY OAS | 2.80% | 15.0 bp | 8.0 bp | -32.0 bp | Credit spread stress |
| IG OAS | 0.76% | 2.0 bp | 3.0 bp | -10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.51 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.58 pp | n/a | EM relative stress |

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

- R1 continuation: **not confirmed**
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

