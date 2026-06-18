import subprocess
import os

def run_desktop_searches():
    print("\n🔍 Starting Desktop Searches...")
    subprocess.run(["python3", "bing_desktop_search.py"])

def run_mobile_searches():
    print("\n📱 Starting Mobile Searches...")
    subprocess.run(["python3", "bing_mobile_search.py"])

def run_all_searches():
    run_desktop_searches()
    run_mobile_searches()
    print("\n✅ All searches complete!")

def dag_local():
    os.environ["DAGSTER_DBT_PROJECT_ON_LOAD"] = "1"
    os.environ["PYTHONLEGACYWINDOWSSTUDIO"] = "1"
    cmd = ["dagster", "dev", "-m", "dags.definitions", "-h","0.0.0.0", "-p","30303"]
    subprocess.run(cmd)

if __name__ == "__main__":
    run_desktop_searches()
    run_mobile_searches()
    print("\n✅ All searches complete!")
    # dag_local()