# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-12T12:07:26.807393+00:00
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
| DXY | 99.77 | -0.30% | 0.90% | -0.32% | Dollar pressure |
| SPY | 737.76 | -2.55% | -0.61% | 10.28% | Broad risk asset |
| QQQ | 717.12 | -3.17% | 0.34% | 19.01% | High-duration growth |
| IWM | 290.41 | -0.55% | 2.74% | 16.14% | Small-cap financing sensitivity |
| TLT | 85.98 | 0.56% | 1.79% | -0.53% | Long-duration bond stress |
| EEM | 67.50 | -2.32% | 0.43% | 14.89% | EM dollar/rate transmission |
| HYG | 79.94 | 0.14% | 0.55% | 1.69% | Credit market proxy |
| HY OAS | 2.80% | 5.0 bp | 4.0 bp | -47.0 bp | Credit spread stress |
| IG OAS | 0.75% | 1.0 bp | -1.0 bp | -15.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.35 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.04 pp | n/a | EM relative stress |

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

