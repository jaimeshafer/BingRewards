import subprocess

def run_desktop_searches():
    print("\n🔍 Starting Desktop Searches...")
    subprocess.run(["python3", "bing_desktop_search.py"])

def run_mobile_searches():
    print("\n📱 Starting Mobile Searches...")
    subprocess.run(["python3", "bing_mobile_search.py"])

if __name__ == "__main__":
    run_desktop_searches()
    run_mobile_searches()
    print("\n✅ All searches complete!")