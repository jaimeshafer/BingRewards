from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

print("🚀 Launching Daily Set automation...")

# Use your signed-in Chrome profile
user_data_dir = os.path.expanduser("~/chrome-automation-profile")

chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")
# chrome_options.add_argument("--headless")  # Use non-headless to debug

driver = webdriver.Chrome(options=chrome_options)

# Go to Bing Rewards Dashboard
driver.get("https://rewards.bing.com/")

try:
    # Wait for Daily Set section to load
    print("🔎 Waiting for daily sets to load...")
    wait = WebDriverWait(driver, 15)
    
    # Get the daily set tiles (usually 3)
    daily_set = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ds-tiles-container .ds-card"))
    )
    print(f"✅ Found {len(daily_set)} daily set items")

    # Loop through them
    for i, item in enumerate(daily_set):
        try:
            link = item.find_element(By.TAG_NAME, "a")
            href = link.get_attribute("href")
            print(f"🔗 Opening item {i+1}: {href}")
            driver.execute_script("window.open(arguments[0]);", href)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(10)  # Let the quiz/poll load and auto-complete
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f"⚠️ Could not open item {i+1}: {e}")

except Exception as e:
    print("❌ Failed to find daily set items.")
    print(e)

driver.quit()
print("✅ Daily Set automation complete.")
