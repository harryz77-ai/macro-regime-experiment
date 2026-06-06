# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-06-06T09:14:37.562231+00:00
- Latest market date: 2026-06-05
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **55.7%**
- Previous regime: R0
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 100.07 | 1.17% | 1.85% | 0.85% | Dollar pressure |
| SPY | 737.55 | -2.50% | 0.82% | 9.35% | Broad risk asset |
| QQQ | 705.06 | -4.50% | 1.46% | 16.17% | High-duration growth |
| IWM | 281.65 | -3.02% | -0.22% | 11.59% | Small-cap financing sensitivity |
| TLT | 85.06 | -0.43% | -0.30% | -1.25% | Long-duration bond stress |
| EEM | 64.59 | -5.85% | -3.00% | 9.79% | EM dollar/rate transmission |
| HYG | 79.43 | -0.59% | -0.03% | 0.98% | Credit market proxy |
| HY OAS | 2.74% | 2.0 bp | -7.0 bp | -54.0 bp | Credit spread stress |
| IG OAS | 0.74% | 1.0 bp | -5.0 bp | -19.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.03 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.82 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 28.7% | High-rate absorption |
| R1 | 55.7% | Bear steepening + dollar pressure |
| R2 | 6.4% | Credit / sovereign stress spillover |
| R3 | 9.2% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

