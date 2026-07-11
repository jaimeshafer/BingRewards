from dagster import Definitions
from dags.assets import assets
from dags.jobs import jobs
from dags.sensors.schedules import schedules

defs = Definitions(
    assets = assets,
    schedules=schedules,
    jobs=jobs
)