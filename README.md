## BingPoints

Dagster project that runs desktop and mobile Selenium browser assets on a daily schedule.

### Local Setup

Install dependencies:

```bash
poetry install
```

### Run Dagster locally:

`poetry run local`

Or directly:
`poetry run dagster dev -m dags.definitions -h 0.0.0.0 -p 30303`

Open dagster at: [http://localhost:30303](http://localhost:30303)

### Cookie Setup

Run the cookie script manually when cookies need to be created or refreshed:
`poetry run python scripts/save_bing_cookies.py`

This saves cookies to:
`data/bing_cookies.pkl`

Do not commit `data/` or cookie files.

### Docker / Portainer

Build and run locally:
`docker compose up --build`

Run detached:
`docker compose up --build -d`

Stop:
`docker compose down`

Dagster runs at:
[http://localhost:30303](http://localhost:30303)

For Portainer, deploy this repo as a stack using `docker-compose.yml`.

### Environment Variables

```yaml
DAGSTER_HOME=/app/dagster_home
SELENIUM_REMOTE_URL=http://selenium:4444/wd/hub
BING_COOKIES_PATH=/app/data/bing_cookies.pkl
CHROME_PROFILE_DIR=/app/data/chrome-automation-profile
```

### Dagster
Assets:
- desktop_asset
- mobile_asset
  - mobile_asset depends on desktop_asset, so desktop runs first.

Schedule:
- daily_job_schedule
- Cron: 0 3 * * *
