import os
import time
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
    user_data_dir = os.path.expanduser("~/chrome-automation-profile")

    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    context.log.info("Starting desktop searches.")

    for i in range(nsearch):
        word1 = r.word()
        word2 = r.word()
        word3 = r.word()
        query = f"{word1} {word2} {word3}"

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
            driver = webdriver.Chrome(options=chrome_options)
            context.log.info("[%s/%s] Searching: %s", i + 1, nsearch, query)
            driver.get(search_url)

            context.log.info("Sleeping for %s seconds.", delay)
            time.sleep(delay)

        finally:
            if driver:
                driver.quit()

    context.log.info("Desktop searches ended.")