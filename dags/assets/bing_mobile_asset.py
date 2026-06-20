import pickle
import time
from pathlib import Path
from urllib.parse import urlencode

from dagster import AssetExecutionContext, asset
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wonderwords import RandomWord

from dags.utils.time_delay import get_random_delay
from .bing_desktop_asset import desktop_asset


@asset(
    description="This asset runs mobile browser searches using random words.",
    group_name="bing_search",
    kinds={"python"},
    deps=[desktop_asset],
)
def mobile_asset(context: AssetExecutionContext) -> None:
    r = RandomWord()
    nsearch = 24
    cookie_path = Path("bing_cookies.pkl")

    mobile_emulation = {"deviceName": "iPhone X"}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless=new")

    context.log.info("Using mobile emulation with saved cookies.")

    with cookie_path.open("rb") as f:
        cookies = pickle.load(f)

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
            selenium_remote_url = os.getenv("SELENIUM_REMOTE_URL")
            if selenium_remote_url:
                driver = webdriver.Remote(
                    command_executor=selenium_remote_url,
                    options=chrome_options,
                )
            else:
                driver = webdriver.Chrome(options=chrome_options)
                
            driver.get("https://www.bing.com")
            time.sleep(2)

            for cookie in cookies:
                cookie.pop("expiry", None)
                driver.add_cookie(cookie)

            context.log.info("[%s/%s] Searching: %s", i + 1, nsearch, query)
            driver.get(search_url)

            context.log.info("Sleeping for %s seconds.", delay)
            time.sleep(delay)

        except Exception as e:
            context.log.exception("Search %s failed: %s", i + 1, e)

        finally:
            if driver:
                driver.quit()

    context.log.info("Mobile searches ended.")