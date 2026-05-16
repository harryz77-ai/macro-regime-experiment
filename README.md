# Macro Regime Skill Runner

This repo contains:

- `SKILL.md`: fixed methodology and operating discipline.
- `runner.py`: deterministic data fetch + feature engineering + R0/R1/R2/R3 classification.
- `requirements.txt`: Python dependencies.
- `.github/workflows/macro-regime.yml`: scheduled GitHub Actions workflow.

## Local run

```bash
pip install -r requirements.txt
python runner.py --previous-regime R1 \
  --output reports/latest.md \
  --json-output data/latest.json \
  --history-csv data/history.csv
```

## GitHub Actions

1. Push all files to a GitHub repo.
2. Open repo page.
3. Go to **Actions** tab.
4. Enable workflows if GitHub asks.
5. Choose **Macro Regime Daily Update**.
6. Click **Run workflow** once to test.
7. The scheduled run is configured in `.github/workflows/macro-regime.yml`.

## VPS cron

```bash
crontab -e
```

Add:

```cron
30 23 * * 1-5 cd /opt/macro-regime && /usr/bin/python3 runner.py --previous-regime auto --output reports/latest.md --json-output data/latest.json --history-csv data/history.csv >> logs/cron.log 2>&1
```

This uses UTC server time by default. `23:30 UTC` is safely after the US cash market close across daylight-saving changes.
