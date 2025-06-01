# bing_mobile_search.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wonderwords import RandomWord
import time
import random
import pickle

r = RandomWord()
nsearch = 24

# Mobile emulation setup
mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

print("📱 Using mobile emulation with saved cookies...\n")

for i in range(nsearch):
    word1 = r.word()
    word2 = r.word()
    word3 = r.word()
    query = f"{word1} {word2} {word3}"
    search_url = f"https://www.bing.com/search?q={word1}+{word2}+{word3}"
    delay = random.randint(450, 500)

    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.bing.com")
        time.sleep(2)

        # Load cookies
        with open("bing_cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                # Remove expiry to avoid error
                if "expiry" in cookie:
                    del cookie["expiry"]
                driver.add_cookie(cookie)

        driver.get(search_url)
        print(f"[{i+1}/{nsearch}] Searching: {query}")
        time.sleep(delay)

    except Exception as e:
        print(f"Search {i+1} failed: {e}")
    finally:
        if driver:
            driver.quit()

print("\n**ALL DONE** ✅")
