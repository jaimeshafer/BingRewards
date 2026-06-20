<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle

# Mobile emulation setup
mobile_emulation = {"deviceName": "iPhone X"}
=======
import os
import pickle
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


cookie_path = Path("data/bing_cookies.pkl")
cookie_path.parent.mkdir(parents=True, exist_ok=True)

mobile_emulation = {"deviceName": "iPhone X"}

>>>>>>> 353d131 (adding dagster)
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

<<<<<<< HEAD
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.bing.com")

print("👉 Please sign in manually within the browser window.")
input("✅ Press Enter after you're fully signed in...")

# Save cookies to file
with open("bing_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Cookies saved to 'bing_cookies.pkl'")
driver.quit()
=======
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
>>>>>>> 353d131 (adding dagster)
