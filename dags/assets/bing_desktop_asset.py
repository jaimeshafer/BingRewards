import os
import pickle
import time
from pathlib import Path
from urllib.parse import urlencode

from dagster import AssetExecutionContext, asset
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wonderwords import RandomWord

from dags.utils.time_delay import get_random_delay


@asset(
    description="This asset searches as a desktop using random words.",
    group_name="bing_search",
    kinds={"python"},
)
def desktop_asset(context: AssetExecutionContext) -> None:
    r = RandomWord()
    nsearch = 36
    selenium_remote_url = os.getenv("SELENIUM_REMOTE_URL")
    cookie_path = Path(
        os.getenv("BING_DESKTOP_COOKIES_PATH", "data/bing_desktop_cookies.pkl")
    )

    chrome_options = Options()
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    context.log.info("Starting desktop searches.")

    with cookie_path.open("rb") as f:
        cookies = pickle.load(f)

    for i in range(nsearch):
        query = f"{r.word()} {r.word()} {r.word()}"

        search_url = "https://www.bing.com/search?" + urlencode(
            {
                "q": query,
                "qs": "n",
                "form": "QBRE",
                "sp": "-1",
                "lq": "0",
                "pq": query,
                "sc": "10-14",
                "sk": "",
                "cvid": "F958C197B98945529D35B01540AC9449",
                "ghsh": "0",
                "ghacc": "0",
                "ghpl": "",
            }
        )

        delay = get_random_delay()
        driver = None

        try:
            if selenium_remote_url:
                driver = webdriver.Remote(
                    command_executor=selenium_remote_url,
                    options=chrome_options,
                )
            else:
                driver = webdriver.Chrome(options=chrome_options)

            driver.get("https://www.bing.com")
            time.sleep(2)

            skipped_cookies = 0

            for cookie in cookies:
                clean_cookie = dict(cookie)
                clean_cookie.pop("expiry", None)

                try:
                    driver.add_cookie(clean_cookie)
                except Exception:
                    skipped_cookies += 1

            if skipped_cookies:
                context.log.info("Skipped %s cookies that Selenium could not restore.", skipped_cookies)
                                

            context.log.info("[%s/%s] Searching: %s", i + 1, nsearch, query)
            driver.get(search_url)
            time.sleep(10)

            context.log.info("Landed on: %s", driver.current_url)
            context.log.info("Page title: %s", driver.title)

        except Exception as e:
            context.log.exception("Search %s failed: %s", i + 1, e)
            raise

        finally:
            if driver:
                try:
                    driver.quit()
                except Exception as e:
                    context.log.warning("Driver quit failed: %s", e)

        if i < nsearch - 1:
            context.log.info("Sleeping for %s seconds.", delay)
            time.sleep(delay)

    context.log.info("Desktop searches ended.")