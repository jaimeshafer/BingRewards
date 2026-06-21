import os
import pickle
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def save_mobile_cookie():
    cookie_path = Path(os.getenv("BING_MOBILE_COOKIES_PATH", "data/bing_mobile_cookies.pkl"))
    cookie_path.parent.mkdir(parents=True, exist_ok=True)

    mobile_emulation = {"deviceName": "iPhone X"}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    selenium_remote_url = os.getenv("SELENIUM_REMOTE_URL")

    if selenium_remote_url:
        driver = webdriver.Remote(
            command_executor=selenium_remote_url,
            options=chrome_options,
        )
    else:
        driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.bing.com")

        print("Please sign in manually within the browser window.")
        input("Press Enter after you're fully signed in...")

        with cookie_path.open("wb") as f:
            pickle.dump(driver.get_cookies(), f)

        print(f"Cookies saved to {cookie_path}")

    finally:
        driver.quit()

def save_desktop_cookie():
    cookie_path = Path(
        os.getenv("BING_DESKTOP_COOKIES_PATH", "data/bing_desktop_cookies.pkl")
    )
    cookie_path.parent.mkdir(parents=True, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.bing.com")

        print("Please sign in manually within the browser window.")
        input("Press Enter after you're fully signed in...")

        with cookie_path.open("wb") as f:
            pickle.dump(driver.get_cookies(), f)

        print(f"Cookies saved to {cookie_path}")

    finally:
        driver.quit()