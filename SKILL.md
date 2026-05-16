# Macro Regime Data Fetch Skill

## Purpose

This skill defines a repeatable macro-regime monitoring method. It fetches fresh macro-market data, builds a multi-asset observation vector, maps the vector into a 4-state macro regime framework, and outputs a concise monitoring report.

It is designed for:

- macro regime identification
- Markov transition matrix monitoring
- cross-asset stress detection
- R1-to-R2 upgrade alerts
- scenario tree updates
- risk monitoring

It is not an automatic trading system and must not be presented as a buy/sell signal.

---

## Regime Framework

Use four observable macro-financial regimes:

| Regime | Name | Core Features |
|---|---|---|
| R0 | High-rate absorption | Treasury yields high but no longer rising aggressively; equities resilient; dollar stable |
| R1 | Bear steepening + dollar pressure | Long-end yields rising; USD stronger; small caps and EM weak |
| R2 | Credit / sovereign stress spillover | Credit spreads widen; sovereign spreads widen; risk assets deleverage together |
| R3 | Rate decline / policy repair | Yields fall; driven by growth shock or policy/liquidity support |

Always separate:

1. verified market data
2. computed indicators
3. model inference
4. judgment calls
5. monitoring suggestions

---

## Required Data

### US Rates

| Indicator | Preferred Source | Backup Source |
|---|---|---|
| US 2Y Treasury yield | FRED `DGS2` | Yahoo / Treasury |
| US 10Y Treasury yield | FRED `DGS10` | Yahoo `^TNX` |
| US 30Y Treasury yield | FRED `DGS30` | Yahoo `^TYX` |
| 10Y - 2Y curve | FRED `DGS10`, `DGS2` | Treasury / Yahoo |
| 30Y - 10Y curve | FRED `DGS30`, `DGS10` | Treasury / Yahoo |

### Dollar

| Indicator | Preferred Source | Backup Source |
|---|---|---|
| DXY Dollar Index | Yahoo Finance `DX-Y.NYB` | Stooq / MarketWatch |
| UUP ETF | Yahoo Finance `UUP` | Stooq |

### Risk Assets

| Indicator | Ticker |
|---|---|
| S&P 500 proxy | `SPY` |
| Nasdaq proxy | `QQQ` |
| Russell 2000 proxy | `IWM` |
| Long-duration Treasury ETF | `TLT` |
| High-yield bond ETF | `HYG` |
| Emerging markets ETF | `EEM` |
| Investment-grade bond ETF | `LQD` |

### Credit and Sovereign Stress

| Indicator | Preferred Source |
|---|---|
| US High Yield OAS | FRED `BAMLH0A0HYM2` |
| US IG Corporate OAS | FRED `BAMLC0A0CM` |
| Euro area sovereign spread proxy | User-provided CSV/API if available |

If direct sovereign spread data is unavailable, mark it as `missing`, not zero.

---

## Data Freshness Rules

Each report must show:

- fetch timestamp
- latest market date
- source used
- missing fields
- stale fields

Classify freshness:

| Status | Rule |
|---|---|
| Fresh | latest data date within 1 business day |
| Acceptable | latest data date within 3 business days |
| Stale | latest data date older than 3 business days |
| Missing | no reliable data fetched |

Do not infer a crisis regime from stale or missing data.

---

## Observation Window

For each market price or yield, compute:

- latest value
- 5-day change
- 20-day change
- 60-day change

For ETFs and indices, compute percentage returns.

For yields and spreads, compute basis-point changes.

---

## Core Features

The runner should generate this feature dictionary:

```python
features = {
    "us2y_level": latest_2y,
    "us10y_level": latest_10y,
    "us30y_level": latest_30y,
    "us10y_20d_change_bp": change_10y_20d,
    "us30y_20d_change_bp": change_30y_20d,
    "curve_10y2y": us10y - us2y,
    "curve_30y10y": us30y - us10y,
    "dxy_20d_return": dxy_return_20d,
    "spy_20d_return": spy_return_20d,
    "qqq_20d_return": qqq_return_20d,
    "iwm_spy_20d_relative": iwm_return_20d - spy_return_20d,
    "eem_spy_20d_relative": eem_return_20d - spy_return_20d,
    "tlt_20d_return": tlt_return_20d,
    "hyg_20d_return": hyg_return_20d,
    "hy_oas_20d_change_bp": hy_oas_change_20d,
    "ig_oas_20d_change_bp": ig_oas_change_20d,
    "sovereign_spread_change_bp": sovereign_spread_change_20d,
}
```

---

## Regime Scoring Rules

Use score-based Bayesian-style evidence aggregation.

Initialize:

```python
scores = {
    "R0": 0,
    "R1": 0,
    "R2": 0,
    "R3": 0,
}
```

### R0: High-rate absorption

Add R0 evidence when:

- 10Y yield is high but 20-day change is small
- 30Y yield is high but not accelerating
- SPY or QQQ is resilient
- IWM/SPY relative weakness is mild
- DXY is stable
- HY OAS is stable or narrowing

### R1: Bear steepening + dollar pressure

Add R1 evidence when:

- 10Y or 30Y yield rises meaningfully
- 30Y yield rises faster than 10Y
- DXY rises
- TLT falls
- IWM underperforms SPY
- EEM underperforms SPY
- credit spreads are not yet disorderly

### R2: Credit / sovereign stress spillover

Add R2 evidence when:

- HY OAS expands sharply
- HYG falls quickly
- IWM, EEM, HYG, and equities fall together
- DXY spikes
- sovereign spreads widen beyond alert levels
- risk-asset correlation rises during drawdown

### R3: Rate decline / policy repair

Add R3 evidence when:

- 10Y and 30Y yields decline materially
- TLT rises
- DXY weakens
- credit spreads stabilize or narrow
- risk assets recover
- policy-sensitive assets rebound

---

## Probability Conversion

Convert scores into probabilities using softmax.

Recommended default:

```python
temperature = 1.25
```

---

## Markov Prior

Use this 4-state transition matrix as the research prior unless the user provides an updated matrix.

Rows = current state.  
Columns = next state.

```python
transition_matrix = {
    "R0": {"R0": 0.55, "R1": 0.25, "R2": 0.06, "R3": 0.14},
    "R1": {"R0": 0.25, "R1": 0.43, "R2": 0.18, "R3": 0.14},
    "R2": {"R0": 0.10, "R1": 0.18, "R2": 0.38, "R3": 0.34},
    "R3": {"R0": 0.42, "R1": 0.20, "R2": 0.08, "R3": 0.30},
}
```

Combine signal probability and Markov prior as:

```python
posterior = 0.65 * signal_probability + 0.35 * markov_prior_probability
```

If previous regime is unknown, use signal probability only.

---

## Alert Thresholds

### R1 Maintenance

R1 remains likely when:

- 10Y yield is between 4.5% and 5.0%
- 30Y yield is between 5.0% and 5.5%
- DXY rises but EM selling is not disorderly
- HY OAS is stable or only moderately wider
- small caps and EM underperform without systemic credit stress

### R2 Upgrade Warning

Raise R2 warning when:

- 10Y yield remains above 5.0%
- 30Y yield remains above 5.5%
- DXY breaks above 101 with EM weakness
- HY OAS widens sharply
- HYG falls quickly
- OAT/Bund exceeds 100 bp
- BTP/Bund exceeds 180 bp
- small caps, EM, credit, and high-duration equities sell off together

---

## Output Format

Each run should produce:

```markdown
# Macro Regime Update

## 1. Timestamp

- Fetch time:
- Latest market date:
- Data freshness:
- Missing fields:

## 2. Current Regime Conclusion

- Most likely regime:
- Probability:
- Previous regime:
- Markov-adjusted next-month path:

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|

## 4. Regime Probability

| Regime | Probability | Interpretation |
|---|---:|---|

## 5. Risk Alerts

- R1 continuation:
- R2 upgrade warning:
- R3 policy-repair signal:

## 6. Interpretation

Separate:

- verified market data
- model inference
- subjective judgment

## 7. Next Data to Watch

List the 3-5 indicators most likely to change the regime classification.
```

---

## Operating Instructions

When the user says:

- “更新宏观状态”
- “抓一下最新数据”
- “跑一下 Markov macro matrix”
- “现在是 R1 还是 R2”
- “检查有没有升级到信用压力”
- “刷新状态切换模型”

Then run `runner.py`, read `reports/latest.md` or `data/latest.json`, and summarize the result.

---

## Output Discipline

Do not overstate precision.  
Do not infer R2 unless credit or sovereign stress confirms the move.  
Do not infer R3 unless yields fall and liquidity/risk signals improve.  
Do not present the result as a trading recommendation.
