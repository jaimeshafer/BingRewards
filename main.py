import subprocess
import os
from scripts.save_bing_cookies import save_desktop_cookie, save_mobile_cookie

def dag_local():
    os.environ["DAGSTER_DBT_PROJECT_ON_LOAD"] = "1"
    os.environ["PYTHONLEGACYWINDOWSSTUDIO"] = "1"
    
    mkdir = ["mkdir","dagster_home"]
    subprocess.run(mkdir)
    os.environ["DAGSTER_HOME"] = os.path.abspath("dagster_home")

    cmd = ["dagster", "dev", "-m", "dags.definitions", "-h","0.0.0.0", "-p","30303"]
    subprocess.run(cmd)

def save_cookies():
    save_desktop_cookie()
    save_mobile_cookie()