# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-23T01:30:14.592282+00:00
- Latest market date: 2026-06-22
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption**
- Posterior probability: **46.3%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.460% | 1.0 bp | -11.0 bp | 13.0 bp | Long-end rate pressure |
| US 30Y yield | 4.900% | -5.0 bp | -21.0 bp | 1.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.04 | 1.30% | 1.87% | 1.45% | Dollar pressure |
| SPY | 744.39 | 0.61% | 0.48% | 13.62% | Broad risk asset |
| QQQ | 737.95 | 2.30% | 3.28% | 25.54% | High-duration growth |
| IWM | 298.18 | 2.03% | 5.81% | 18.69% | Small-cap financing sensitivity |
| TLT | 86.09 | 0.37% | 2.62% | 0.29% | Long-duration bond stress |
| EEM | 71.21 | 5.45% | 8.41% | 24.66% | EM dollar/rate transmission |
| HYG | 79.94 | 0.00% | 0.56% | 2.19% | Credit market proxy |
| HY OAS | 2.66% | -5.0 bp | -8.0 bp | -80.0 bp | Credit spread stress |
| IG OAS | 0.74% | 0.0 bp | 0.0 bp | -19.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.32 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 7.92 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 46.3% | High-rate absorption |
| R1 | 35.8% | Bear steepening + dollar pressure |
| R2 | 7.6% | Credit / sovereign stress spillover |
| R3 | 10.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

