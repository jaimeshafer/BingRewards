from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wonderwords import RandomWord
import time
import random
import os

r = RandomWord()

print("\nStarting!!!")
# nsearch = int(input("\nEnter number of searches ==> "))
nsearch = 36

print("\nHang On!!")

# Use cloned Chrome profile to stay signed in (same one used for mobile)
user_data_dir = os.path.expanduser("~/chrome-automation-profile")

for i in range(nsearch):
    word1 = r.word()
    word2 = r.word()
    word3 = r.word()
    query = f"{word1} {word2} {word3}"
    search_url = f"https://www.bing.com/search?q="+word1+"+"+word2+"+"+word3+"&qs=n&form=QBRE&sp=-1&lq=0&pq="+word1+"+"+word2+"+"+word3+"&sc=10-14&sk=&cvid=F958C197B98945529D35B01540AC9449&ghsh=0&ghacc=0&ghpl="

    delay = random.randint(450, 500)

    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    # Optional: keep Chrome visible
    chrome_options.add_argument("--headless")  # Only if you want to hide the window

    driver = webdriver.Chrome(options=chrome_options)
    print(f"[{i+1}/{nsearch}] Searching: {query}")
    driver.get(search_url)

    time.sleep(delay)
    driver.quit()

print("\n**ENDED** ✅")
