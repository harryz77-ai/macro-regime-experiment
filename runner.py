#!/usr/bin/env python3
"""
Macro Regime Runner

Fetches macro-market data, computes a cross-asset observation vector,
classifies the current R0/R1/R2/R3 regime, and writes Markdown + JSON outputs.

Default design:
- No LLM call
- No token consumption
- Data + scoring are deterministic
- Suitable for GitHub Actions or VPS cron

Install:
    pip install -r requirements.txt

Run:
    python runner.py --previous-regime R1 \
      --output reports/latest.md \
      --json-output data/latest.json \
      --history-csv data/history.csv
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional, Any, List, Tuple

import numpy as np
import pandas as pd


FRED_SERIES = {
    "us2y": "DGS2",
    "us10y": "DGS10",
    "us30y": "DGS30",
    "hy_oas": "BAMLH0A0HYM2",
    "ig_oas": "BAMLC0A0CM",
}

YAHOO_TICKERS = {
    "dxy": "DX-Y.NYB",
    "spy": "SPY",
    "qqq": "QQQ",
    "iwm": "IWM",
    "tlt": "TLT",
    "uup": "UUP",
    "eem": "EEM",
    "hyg": "HYG",
    "lqd": "LQD",
}

REGIME_NAMES = {
    "R0": "High-rate absorption",
    "R1": "Bear steepening + dollar pressure",
    "R2": "Credit / sovereign stress spillover",
    "R3": "Rate decline / policy repair",
}

TRANSITION_MATRIX = {
    "R0": {"R0": 0.55, "R1": 0.25, "R2": 0.06, "R3": 0.14},
    "R1": {"R0": 0.25, "R1": 0.43, "R2": 0.18, "R3": 0.14},
    "R2": {"R0": 0.10, "R1": 0.18, "R2": 0.38, "R3": 0.34},
    "R3": {"R0": 0.42, "R1": 0.20, "R2": 0.08, "R3": 0.30},
}


@dataclass
class SeriesResult:
    name: str
    source: str
    series: Optional[pd.Series]
    error: Optional[str] = None


def import_optional_modules():
    modules = {}

    try:
        import yfinance as yf  # type: ignore
        modules["yf"] = yf
    except Exception as exc:
        modules["yf"] = None
        modules["yf_error"] = str(exc)

    return modules

def clean_series(series: pd.Series) -> pd.Series:
    series = pd.to_numeric(series, errors="coerce").dropna()
    series.index = pd.to_datetime(series.index)
    series = series.sort_index()
    return series


def fetch_fred_series(name: str, series_id: str, start: str) -> SeriesResult:
    """
    Fetch a FRED series through FRED's public CSV endpoint.

    This avoids pandas_datareader, which can break when pandas changes
    internal utility APIs.
    """
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"

    try:
        df = pd.read_csv(url)

        if df.empty:
            return SeriesResult(name, f"FRED:{series_id}", None, f"No data returned for {series_id}")

        if "observation_date" in df.columns:
            date_col = "observation_date"
        elif "DATE" in df.columns:
            date_col = "DATE"
        else:
            return SeriesResult(name, f"FRED:{series_id}", None, f"No date column found for {series_id}")

        if series_id in df.columns:
            value_col = series_id
        else:
            value_candidates = [c for c in df.columns if c != date_col]
            if not value_candidates:
                return SeriesResult(name, f"FRED:{series_id}", None, f"No value column found for {series_id}")
            value_col = value_candidates[0]

        dates = pd.to_datetime(df[date_col], errors="coerce")
        values = pd.to_numeric(df[value_col].replace(".", np.nan), errors="coerce")

        s = pd.Series(values.to_numpy(), index=dates).dropna().sort_index()

        if start:
            s = s[s.index >= pd.Timestamp(start)]

        if s.empty:
            return SeriesResult(name, f"FRED:{series_id}", None, f"No non-missing observations after {start}")

        return SeriesResult(name, f"FRED:{series_id}", clean_series(s), None)

    except Exception as exc:
        return SeriesResult(name, f"FRED:{series_id}", None, str(exc))


def fetch_yahoo_series(ticker: str, period: str, yf: Any) -> Tuple[Optional[pd.Series], Optional[str]]:
    if yf is None:
        return None, "yfinance is not installed"

    try:
        df = yf.download(
            ticker,
            period=period,
            auto_adjust=True,
            progress=False,
            threads=False,
        )
        if df is None or df.empty:
            return None, f"No Yahoo data returned for {ticker}"

        if isinstance(df.columns, pd.MultiIndex):
            if ("Close", ticker) in df.columns:
                raw = df[("Close", ticker)]
            else:
                # yfinance sometimes returns MultiIndex even for one ticker.
                raw = df.xs("Close", axis=1, level=0).iloc[:, 0]
        else:
            raw = df["Close"]

        return clean_series(raw), None
    except Exception as exc:
        return None, str(exc)


def fetch_yahoo_data(tickers: Dict[str, str], period: str, yf: Any) -> Dict[str, SeriesResult]:
    results: Dict[str, SeriesResult] = {}
    for name, ticker in tickers.items():
        s, err = fetch_yahoo_series(ticker, period, yf)
        results[name] = SeriesResult(name, f"Yahoo:{ticker}", s, err)
    return results


def latest(series: Optional[pd.Series]) -> Optional[float]:
    if series is None or series.empty:
        return None
    return float(series.iloc[-1])


def latest_date(series: Optional[pd.Series]) -> Optional[str]:
    if series is None or series.empty:
        return None
    return pd.Timestamp(series.index[-1]).date().isoformat()


def pct_change(series: Optional[pd.Series], days: int) -> Optional[float]:
    if series is None or len(series) <= days:
        return None
    return float((series.iloc[-1] / series.iloc[-days - 1] - 1.0) * 100.0)


def bp_change(series: Optional[pd.Series], days: int) -> Optional[float]:
    """
    FRED yields and OAS are percent values, so percentage-point changes
    are converted to basis points by multiplying by 100.
    """
    if series is None or len(series) <= days:
        return None
    return float((series.iloc[-1] - series.iloc[-days - 1]) * 100.0)


def safe_subtract(a: Optional[float], b: Optional[float]) -> Optional[float]:
    if a is None or b is None:
        return None
    return float(a - b)


def business_days_old(date_str: Optional[str]) -> Optional[int]:
    if date_str is None:
        return None
    today = pd.Timestamp.utcnow().normalize().tz_localize(None)
    d = pd.Timestamp(date_str).normalize().tz_localize(None)
    if d > today:
        return 0
    # Count business days strictly after the data date through today.
    days = pd.bdate_range(d + pd.Timedelta(days=1), today)
    return int(len(days))


def freshness_from_date(date_str: Optional[str]) -> str:
    age = business_days_old(date_str)
    if age is None:
        return "Missing"
    if age <= 1:
        return "Fresh"
    if age <= 3:
        return "Acceptable"
    return "Stale"


def add_score(condition: bool, scores: Dict[str, int], regime: str, points: int = 1) -> None:
    if condition:
        scores[regime] += points


def softmax(scores: Dict[str, int], temperature: float = 1.25) -> Dict[str, float]:
    labels = list(scores.keys())
    values = np.array([scores[k] for k in labels], dtype=float) / float(temperature)
    exp_values = np.exp(values - np.max(values))
    probs = exp_values / exp_values.sum()
    return {k: float(v) for k, v in zip(labels, probs)}


def build_features(
    fred: Dict[str, SeriesResult],
    yahoo: Dict[str, SeriesResult],
    sovereign_spread_change_bp: Optional[float] = None,
) -> Dict[str, Optional[float]]:
    features: Dict[str, Optional[float]] = {}

    features["us2y_level"] = latest(fred.get("us2y").series if fred.get("us2y") else None)
    features["us10y_level"] = latest(fred.get("us10y").series if fred.get("us10y") else None)
    features["us30y_level"] = latest(fred.get("us30y").series if fred.get("us30y") else None)

    features["us10y_5d_change_bp"] = bp_change(fred.get("us10y").series if fred.get("us10y") else None, 5)
    features["us10y_20d_change_bp"] = bp_change(fred.get("us10y").series if fred.get("us10y") else None, 20)
    features["us10y_60d_change_bp"] = bp_change(fred.get("us10y").series if fred.get("us10y") else None, 60)

    features["us30y_5d_change_bp"] = bp_change(fred.get("us30y").series if fred.get("us30y") else None, 5)
    features["us30y_20d_change_bp"] = bp_change(fred.get("us30y").series if fred.get("us30y") else None, 20)
    features["us30y_60d_change_bp"] = bp_change(fred.get("us30y").series if fred.get("us30y") else None, 60)

    features["curve_10y2y"] = safe_subtract(features["us10y_level"], features["us2y_level"])
    features["curve_30y10y"] = safe_subtract(features["us30y_level"], features["us10y_level"])

    features["hy_oas_level"] = latest(fred.get("hy_oas").series if fred.get("hy_oas") else None)
    features["ig_oas_level"] = latest(fred.get("ig_oas").series if fred.get("ig_oas") else None)

    features["hy_oas_5d_change_bp"] = bp_change(fred.get("hy_oas").series if fred.get("hy_oas") else None, 5)
    features["hy_oas_20d_change_bp"] = bp_change(fred.get("hy_oas").series if fred.get("hy_oas") else None, 20)
    features["hy_oas_60d_change_bp"] = bp_change(fred.get("hy_oas").series if fred.get("hy_oas") else None, 60)

    features["ig_oas_5d_change_bp"] = bp_change(fred.get("ig_oas").series if fred.get("ig_oas") else None, 5)
    features["ig_oas_20d_change_bp"] = bp_change(fred.get("ig_oas").series if fred.get("ig_oas") else None, 20)
    features["ig_oas_60d_change_bp"] = bp_change(fred.get("ig_oas").series if fred.get("ig_oas") else None, 60)

    for name, result in yahoo.items():
        s = result.series
        features[f"{name}_latest"] = latest(s)
        features[f"{name}_5d_return"] = pct_change(s, 5)
        features[f"{name}_20d_return"] = pct_change(s, 20)
        features[f"{name}_60d_return"] = pct_change(s, 60)

    features["iwm_spy_20d_relative"] = safe_subtract(
        features.get("iwm_20d_return"),
        features.get("spy_20d_return"),
    )
    features["eem_spy_20d_relative"] = safe_subtract(
        features.get("eem_20d_return"),
        features.get("spy_20d_return"),
    )
    features["qqq_spy_20d_relative"] = safe_subtract(
        features.get("qqq_20d_return"),
        features.get("spy_20d_return"),
    )

    features["sovereign_spread_change_bp"] = sovereign_spread_change_bp

    return features


def classify_regime(
    features: Dict[str, Optional[float]],
    previous_regime: Optional[str] = None,
    temperature: float = 1.25,
) -> Dict[str, Any]:
    scores = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}
    evidence: Dict[str, List[str]] = {"R0": [], "R1": [], "R2": [], "R3": []}

    def record(regime: str, condition: bool, text: str, points: int = 1) -> None:
        if condition:
            scores[regime] += points
            evidence[regime].append(text if points == 1 else f"{text} (+{points})")

    us10y = features.get("us10y_level")
    us30y = features.get("us30y_level")
    us10y_20d = features.get("us10y_20d_change_bp")
    us30y_20d = features.get("us30y_20d_change_bp")
    dxy_20d = features.get("dxy_20d_return")
    spy_20d = features.get("spy_20d_return")
    qqq_20d = features.get("qqq_20d_return")
    iwm_spy = features.get("iwm_spy_20d_relative")
    eem_spy = features.get("eem_spy_20d_relative")
    tlt_20d = features.get("tlt_20d_return")
    hyg_20d = features.get("hyg_20d_return")
    hy_oas_20d = features.get("hy_oas_20d_change_bp")
    sov_20d = features.get("sovereign_spread_change_bp")

    # R0
    record("R0", us10y is not None and us10y >= 4.0 and us10y_20d is not None and abs(us10y_20d) < 20,
           "10Y yield is high but not accelerating")
    record("R0", spy_20d is not None and spy_20d > 0 and hy_oas_20d is not None and hy_oas_20d < 20,
           "equity resilience with stable credit")
    record("R0", dxy_20d is not None and abs(dxy_20d) < 1.0,
           "DXY is stable")

    # R1
    record("R1", us10y_20d is not None and us10y_20d > 20,
           "10Y yield rose meaningfully over 20D")
    record("R1", us30y_20d is not None and us30y_20d > 25,
           "30Y yield rose meaningfully over 20D")
    record("R1", dxy_20d is not None and dxy_20d > 1.0,
           "DXY strengthened over 20D")
    record("R1", iwm_spy is not None and iwm_spy < -2.0,
           "IWM underperformed SPY over 20D")
    record("R1", eem_spy is not None and eem_spy < -2.0,
           "EEM underperformed SPY over 20D")
    record("R1", tlt_20d is not None and tlt_20d < -3.0,
           "TLT sold off over 20D")
    record("R1", hy_oas_20d is not None and hy_oas_20d < 50,
           "credit spread pressure is not yet disorderly")

    # R2
    record("R2", hy_oas_20d is not None and hy_oas_20d > 75,
           "HY OAS widened sharply over 20D", 2)
    record("R2", hyg_20d is not None and hyg_20d < -3.0,
           "HYG sold off quickly over 20D")
    record("R2", spy_20d is not None and iwm_spy is not None and spy_20d < -5.0 and iwm_spy < -3.0,
           "broad equity drawdown plus small-cap underperformance")
    record("R2", dxy_20d is not None and eem_spy is not None and dxy_20d > 3.0 and eem_spy < -4.0,
           "DXY spike plus EM underperformance")
    record("R2", sov_20d is not None and sov_20d > 40,
           "sovereign spread widened sharply", 2)

    # R3
    record("R3", us10y_20d is not None and us30y_20d is not None and us10y_20d < -25 and us30y_20d < -25,
           "10Y and 30Y yields fell materially over 20D")
    record("R3", tlt_20d is not None and tlt_20d > 4.0,
           "TLT rallied over 20D")
    record("R3", dxy_20d is not None and dxy_20d < -1.5,
           "DXY weakened over 20D")
    record("R3", hy_oas_20d is not None and hy_oas_20d < -25,
           "HY OAS narrowed over 20D")
    record("R3", spy_20d is not None and qqq_20d is not None and spy_20d > 3.0 and qqq_20d > 3.0,
           "SPY and QQQ rallied over 20D")

    signal_probs = softmax(scores, temperature=temperature)

    if previous_regime in TRANSITION_MATRIX:
        prior = TRANSITION_MATRIX[previous_regime]
        posterior = {
            k: float(0.65 * signal_probs[k] + 0.35 * prior[k])
            for k in signal_probs
        }
    else:
        prior = None
        posterior = signal_probs.copy()

    top_regime = max(posterior, key=posterior.get)

    return {
        "scores": scores,
        "evidence": evidence,
        "signal_probability": signal_probs,
        "markov_prior": prior,
        "posterior_probability": posterior,
        "top_regime": top_regime,
    }


def fmt_num(x: Optional[float], digits: int = 2, suffix: str = "") -> str:
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "missing"
    return f"{x:.{digits}f}{suffix}"


def probability_table(probs: Dict[str, float]) -> str:
    rows = ["| Regime | Probability | Interpretation |", "|---|---:|---|"]
    for regime in ["R0", "R1", "R2", "R3"]:
        rows.append(f"| {regime} | {probs.get(regime, 0.0):.1%} | {REGIME_NAMES[regime]} |")
    return "\n".join(rows)


def build_metadata(fred: Dict[str, SeriesResult], yahoo: Dict[str, SeriesResult]) -> Dict[str, Any]:
    items = {}
    for group_name, group in [("fred", fred), ("yahoo", yahoo)]:
        for name, result in group.items():
            d = latest_date(result.series)
            items[name] = {
                "group": group_name,
                "source": result.source,
                "latest_date": d,
                "freshness": freshness_from_date(d),
                "error": result.error,
            }
    missing = [k for k, v in items.items() if v["latest_date"] is None]
    stale = [k for k, v in items.items() if v["freshness"] == "Stale"]
    latest_dates = [v["latest_date"] for v in items.values() if v["latest_date"] is not None]
    max_date = max(latest_dates) if latest_dates else None
    return {
        "items": items,
        "missing": missing,
        "stale": stale,
        "latest_market_date": max_date,
        "overall_freshness": freshness_from_date(max_date),
    }


def build_evidence_table(features: Dict[str, Optional[float]]) -> str:
    rows = [
        "| Indicator | Latest | 5D | 20D | 60D | Regime Signal |",
        "|---|---:|---:|---:|---:|---|",
    ]

    rows.append(
        f"| US 10Y yield | {fmt_num(features.get('us10y_level'), 3, '%')} | "
        f"{fmt_num(features.get('us10y_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us10y_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us10y_60d_change_bp'), 1, ' bp')} | Long-end rate pressure |"
    )
    rows.append(
        f"| US 30Y yield | {fmt_num(features.get('us30y_level'), 3, '%')} | "
        f"{fmt_num(features.get('us30y_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us30y_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us30y_60d_change_bp'), 1, ' bp')} | Term premium / fiscal supply pressure |"
    )
    rows.append(
        f"| DXY | {fmt_num(features.get('dxy_latest'), 2)} | "
        f"{fmt_num(features.get('dxy_5d_return'), 2, '%')} | "
        f"{fmt_num(features.get('dxy_20d_return'), 2, '%')} | "
        f"{fmt_num(features.get('dxy_60d_return'), 2, '%')} | Dollar pressure |"
    )
    for name, label, signal in [
        ("spy", "SPY", "Broad risk asset"),
        ("qqq", "QQQ", "High-duration growth"),
        ("iwm", "IWM", "Small-cap financing sensitivity"),
        ("tlt", "TLT", "Long-duration bond stress"),
        ("eem", "EEM", "EM dollar/rate transmission"),
        ("hyg", "HYG", "Credit market proxy"),
    ]:
        rows.append(
            f"| {label} | {fmt_num(features.get(f'{name}_latest'), 2)} | "
            f"{fmt_num(features.get(f'{name}_5d_return'), 2, '%')} | "
            f"{fmt_num(features.get(f'{name}_20d_return'), 2, '%')} | "
            f"{fmt_num(features.get(f'{name}_60d_return'), 2, '%')} | {signal} |"
        )

    rows.append(
        f"| HY OAS | {fmt_num(features.get('hy_oas_level'), 2, '%')} | "
        f"{fmt_num(features.get('hy_oas_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('hy_oas_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('hy_oas_60d_change_bp'), 1, ' bp')} | Credit spread stress |"
    )
    rows.append(
        f"| IG OAS | {fmt_num(features.get('ig_oas_level'), 2, '%')} | "
        f"{fmt_num(features.get('ig_oas_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('ig_oas_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('ig_oas_60d_change_bp'), 1, ' bp')} | Investment-grade credit stress |"
    )
    rows.append(
        f"| IWM - SPY relative | n/a | n/a | "
        f"{fmt_num(features.get('iwm_spy_20d_relative'), 2, ' pp')} | n/a | Small-cap relative stress |"
    )
    rows.append(
        f"| EEM - SPY relative | n/a | n/a | "
        f"{fmt_num(features.get('eem_spy_20d_relative'), 2, ' pp')} | n/a | EM relative stress |"
    )

    return "\n".join(rows)


def build_alerts(features: Dict[str, Optional[float]], classification: Dict[str, Any]) -> Dict[str, str]:
    r2_prob = classification["posterior_probability"].get("R2", 0.0)

    us10y = features.get("us10y_level")
    us30y = features.get("us30y_level")
    dxy = features.get("dxy_latest")
    eem_spy = features.get("eem_spy_20d_relative")
    hy_oas_20d = features.get("hy_oas_20d_change_bp")
    hyg_20d = features.get("hyg_20d_return")
    iwm_spy = features.get("iwm_spy_20d_relative")

    r1_conditions = [
        us10y is not None and 4.5 <= us10y <= 5.0,
        us30y is not None and 5.0 <= us30y <= 5.5,
        hy_oas_20d is not None and hy_oas_20d < 50,
        iwm_spy is not None and iwm_spy < 0,
    ]
    r2_conditions = [
        us10y is not None and us10y > 5.0,
        us30y is not None and us30y > 5.5,
        dxy is not None and dxy > 101 and eem_spy is not None and eem_spy < -4,
        hy_oas_20d is not None and hy_oas_20d > 75,
        hyg_20d is not None and hyg_20d < -3.0,
        r2_prob >= 0.30,
    ]
    r3_conditions = [
        features.get("us10y_20d_change_bp") is not None and features["us10y_20d_change_bp"] < -25,
        features.get("us30y_20d_change_bp") is not None and features["us30y_20d_change_bp"] < -25,
        features.get("tlt_20d_return") is not None and features["tlt_20d_return"] > 4,
        hy_oas_20d is not None and hy_oas_20d < -25,
    ]

    return {
        "R1 continuation": "ON" if sum(r1_conditions) >= 2 else "not confirmed",
        "R2 upgrade warning": "ON" if any(r2_conditions) else "not confirmed",
        "R3 policy-repair signal": "ON" if sum(r3_conditions) >= 2 else "not confirmed",
    }


def generate_markdown(report: Dict[str, Any]) -> str:
    features = report["features"]
    classification = report["classification"]
    metadata = report["metadata"]
    alerts = report["alerts"]
    top = classification["top_regime"]
    probs = classification["posterior_probability"]

    evidence_lines = []
    for regime in ["R0", "R1", "R2", "R3"]:
        ev = classification["evidence"].get(regime, [])
        if ev:
            evidence_lines.append(f"- **{regime}**: " + "; ".join(ev))
        else:
            evidence_lines.append(f"- **{regime}**: no strong evidence")

    missing = ", ".join(metadata["missing"]) if metadata["missing"] else "none"
    stale = ", ".join(metadata["stale"]) if metadata["stale"] else "none"

    prior_text = ""
    if classification.get("markov_prior"):
        prior_text = probability_table(classification["markov_prior"])
    else:
        prior_text = "No Markov prior used because previous regime is unknown or invalid."

    md = f"""# Macro Regime Update

## 1. Timestamp

- Fetch time UTC: {report["fetch_time_utc"]}
- Latest market date: {metadata["latest_market_date"]}
- Overall data freshness: {metadata["overall_freshness"]}
- Missing fields: {missing}
- Stale fields: {stale}

## 2. Current Regime Conclusion

- Most likely regime: **{top} — {REGIME_NAMES[top]}**
- Posterior probability: **{probs[top]:.1%}**
- Previous regime: {report.get("previous_regime") or "unknown"}
- Model type: deterministic feature scoring + optional Markov prior

## 3. Evidence Table

{build_evidence_table(features)}

## 4. Regime Probability

{probability_table(probs)}

## 5. Signal Evidence

{chr(10).join(evidence_lines)}

## 6. Markov Prior

{prior_text}

## 7. Risk Alerts

- R1 continuation: **{alerts["R1 continuation"]}**
- R2 upgrade warning: **{alerts["R2 upgrade warning"]}**
- R3 policy-repair signal: **{alerts["R3 policy-repair signal"]}**

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

"""
    return md


def append_history(history_csv: Path, report: Dict[str, Any]) -> None:
    row = {
        "fetch_time_utc": report["fetch_time_utc"],
        "latest_market_date": report["metadata"]["latest_market_date"],
        "previous_regime": report.get("previous_regime"),
        "top_regime": report["classification"]["top_regime"],
    }
    for regime, prob in report["classification"]["posterior_probability"].items():
        row[f"prob_{regime}"] = prob
    for key in [
        "us10y_level", "us30y_level", "us10y_20d_change_bp", "us30y_20d_change_bp",
        "dxy_20d_return", "spy_20d_return", "qqq_20d_return", "iwm_spy_20d_relative",
        "eem_spy_20d_relative", "tlt_20d_return", "hyg_20d_return", "hy_oas_20d_change_bp",
        "ig_oas_20d_change_bp",
    ]:
        row[key] = report["features"].get(key)

    history_csv.parent.mkdir(parents=True, exist_ok=True)
    df_new = pd.DataFrame([row])
    if history_csv.exists():
        df_old = pd.read_csv(history_csv)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new
    df.to_csv(history_csv, index=False)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run macro regime monitoring.")
    parser.add_argument("--previous-regime", default=None, choices=[None, "R0", "R1", "R2", "R3", "auto"], help="Previous regime for Markov prior.")
    parser.add_argument("--output", default="reports/latest.md", help="Markdown report output path.")
    parser.add_argument("--json-output", default="data/latest.json", help="JSON output path.")
    parser.add_argument("--history-csv", default="data/history.csv", help="History CSV path.")
    parser.add_argument("--start", default="2023-01-01", help="Start date for FRED data.")
    parser.add_argument("--period", default="1y", help="Yahoo Finance lookback period.")
    parser.add_argument("--temperature", type=float, default=1.25, help="Softmax temperature.")
    args = parser.parse_args()

    modules = import_optional_modules()

    previous_regime = args.previous_regime
    if previous_regime == "auto":
        hist = Path(args.history_csv)
        if hist.exists():
            try:
                df_hist = pd.read_csv(hist)
                previous_regime = str(df_hist.iloc[-1]["top_regime"])
            except Exception:
                previous_regime = None
        else:
            previous_regime = None

    fred = {
        name: fetch_fred_series(name, series_id, args.start)
        for name, series_id in FRED_SERIES.items()
    }
    yahoo = fetch_yahoo_data(YAHOO_TICKERS, args.period, modules.get("yf"))

    features = build_features(fred, yahoo, sovereign_spread_change_bp=None)
    classification = classify_regime(features, previous_regime=previous_regime, temperature=args.temperature)
    metadata = build_metadata(fred, yahoo)
    alerts = build_alerts(features, classification)

    report: Dict[str, Any] = {
        "fetch_time_utc": datetime.now(timezone.utc).isoformat(),
        "previous_regime": previous_regime,
        "features": features,
        "classification": classification,
        "metadata": metadata,
        "alerts": alerts,
    }

    output = Path(args.output)
    json_output = Path(args.json_output)
    history_csv = Path(args.history_csv)

    output.parent.mkdir(parents=True, exist_ok=True)
    json_output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(generate_markdown(report), encoding="utf-8")
    json_output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    append_history(history_csv, report)

    print(f"Wrote Markdown report: {output}")
    print(f"Wrote JSON report: {json_output}")
    print(f"Updated history CSV: {history_csv}")
    print(f"Top regime: {classification['top_regime']} ({classification['posterior_probability'][classification['top_regime']]:.1%})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
