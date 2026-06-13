# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-13T10:13:50.489563+00:00
- Latest market date: 2026-06-12
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **37.5%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.75 | -0.32% | 0.88% | -0.34% | Dollar pressure |
| SPY | 741.75 | 0.57% | -0.86% | 12.45% | Broad risk asset |
| QQQ | 721.34 | 2.31% | 0.22% | 21.41% | High-duration growth |
| IWM | 292.95 | 4.01% | 2.99% | 19.08% | Small-cap financing sensitivity |
| TLT | 85.77 | 0.83% | 1.40% | -0.22% | Long-duration bond stress |
| EEM | 67.88 | 5.09% | 0.74% | 17.93% | EM dollar/rate transmission |
| HYG | 79.94 | 0.64% | 0.63% | 2.22% | Credit market proxy |
| HY OAS | 2.78% | 4.0 bp | -2.0 bp | -46.0 bp | Credit spread stress |
| IG OAS | 0.75% | 1.0 bp | 0.0 bp | -13.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.85 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.60 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 31.2% | High-rate absorption |
| R1 | 37.5% | Bear steepening + dollar pressure |
| R2 | 16.4% | Credit / sovereign stress spillover |
| R3 | 15.0% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

