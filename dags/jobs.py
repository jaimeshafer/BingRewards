from dagster import AssetSelection,define_asset_job

daily_job = define_asset_job(
    name="daily_job",
    selection=AssetSelection.groups("bing_search")
)

jobs = [
    daily_job,
]