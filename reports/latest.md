# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: 2026-07-28T00:53:58.150402+00:00
- Latest market date: 2026-07-27
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
| US 10Y yield | 4.690% | 14.0 bp | 29.0 bp | 33.0 bp | Long-end rate pressure |
| US 30Y yield | 5.160% | 10.0 bp | 30.0 bp | 22.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.51 | 0.75% | 0.07% | 2.93% | Dollar pressure |
| SPY | 739.09 | -0.57% | 0.65% | 4.12% | Broad risk asset |
| QQQ | 682.12 | -1.90% | -4.78% | 3.85% | High-duration growth |
| IWM | 292.91 | -0.38% | -2.01% | 7.19% | Small-cap financing sensitivity |
| TLT | 83.75 | -0.91% | -3.77% | -1.93% | Long-duration bond stress |
| EEM | 63.62 | 0.52% | -6.39% | 1.53% | EM dollar/rate transmission |
| HYG | 79.27 | -0.48% | -0.30% | 0.08% | Credit market proxy |
| HY OAS | 2.79% | 6.0 bp | -4.0 bp | 1.0 bp | Credit spread stress |
| IG OAS | 0.80% | 1.0 bp | 3.0 bp | 0.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.66 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.04 pp | n/a | EM relative stress |

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

