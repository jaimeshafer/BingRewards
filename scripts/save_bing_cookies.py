from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle

# Mobile emulation setup
mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.bing.com")

print("👉 Please sign in manually within the browser window.")
input("✅ Press Enter after you're fully signed in...")

# Save cookies to file
with open("bing_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Cookies saved to 'bing_cookies.pkl'")
driver.quit()
