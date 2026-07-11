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

Cookies are saved separately for desktop and mobile browser sessions.

When running locally with a visible Chrome browser:

```shell
    poetry run python -c "from scripts.save_bing_cookies import save_desktop_cookie; save_desktop_cookie()"
    poetry run python -c "from scripts.save_bing_cookies import save_mobile_cookie; save_mobile_cookie()"
```

When running in Docker, start the stack first:

    docker compose up --build -d

Open the Selenium noVNC browser:

    http://localhost:7900


Then run desktop cookie setup:

```shell
    docker exec -it bing-points-dagster /app/.venv/bin/python -u -c "from scripts.save_bing_cookies import save_desktop_cookie; save_desktop_cookie()"

```

Sign in through noVNC, then return to the terminal and press Enter.

Then run mobile cookie setup:

```shell
    docker exec -it bing-points-dagster /app/.venv/bin/python -u -c "from scripts.save_bing_cookies import save_mobile_cookie; save_mobile_cookie()"
```

Sign in through noVNC, then return to the terminal and press Enter.

This saves:

```
    data/bing_desktop_cookies.pkl
    data/bing_mobile_cookies.pkl
```

Do not commit `data/` or cookie files.

### Environment Variables
  
  ```yaml
    DAGSTER_HOME=/app/dagster_home
    SELENIUM_REMOTE_URL=http://selenium:4444/wd/hub
    BING_DESKTOP_COOKIES_PATH=/app/data/bing_desktop_cookies.pkl
    BING_MOBILE_COOKIES_PATH=/app/data/bing_mobile_cookies.pkl
  ```

### Headless Mode

The scheduled Dagster assets run Chrome in headless mode.

Cookie setup should be done with a visible browser:

- Locally, the cookie script opens a normal Chrome window.
- In Docker, use Selenium noVNC at `http://localhost:7900`.

Do not use headless mode for the manual login step, because you need to complete sign-in interactively before cookies are saved.

### Raspberry Pi / Remote Host

On a Raspberry Pi or remote host, replace `localhost` with the device IP.


### Dagster

Assets:
- desktop_asset
- mobile_asset
  - mobile_asset depends on desktop_asset, so desktop runs first.

Schedule:
- daily_job_schedule
- Cron: 0 3 * * *
