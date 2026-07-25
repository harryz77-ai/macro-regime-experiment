# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-25T01:02:27.024756+00:00
- Latest market date: 2026-07-24
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure**
- Posterior probability: **76.5%**
- Previous regime: R1
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.710% | 14.0 bp | 30.0 bp | 36.0 bp | Long-end rate pressure |
| US 30Y yield | 5.170% | 8.0 bp | 31.0 bp | 23.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.46 | 0.71% | 0.03% | 2.88% | Dollar pressure |
| SPY | 738.93 | -0.59% | 0.63% | 4.09% | Broad risk asset |
| QQQ | 684.23 | -1.60% | -4.49% | 4.17% | High-duration growth |
| IWM | 291.17 | -0.98% | -2.59% | 6.55% | Small-cap financing sensitivity |
| TLT | 83.25 | -1.50% | -4.34% | -2.52% | Long-duration bond stress |
| EEM | 63.33 | 0.06% | -6.81% | 1.06% | EM dollar/rate transmission |
| HYG | 79.23 | -0.53% | -0.35% | 0.03% | Credit market proxy |
| HY OAS | 2.77% | 6.0 bp | -1.0 bp | 0.0 bp | Credit spread stress |
| IG OAS | 0.79% | 1.0 bp | 3.0 bp | -2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.22 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.44 pp | n/a | EM relative stress |

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|
| R0 | 11.3% | High-rate absorption |
| R1 | 76.5% | Bear steepening + dollar pressure |
| R2 | 6.8% | Credit / sovereign stress spillover |
| R3 | 5.4% | Rate decline / policy repair |

## 5. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

