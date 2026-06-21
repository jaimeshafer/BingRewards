from dagster import Definitions
from .assets import assets
from .jobs import jobs
from .sensors.schedules import schedules

defs = Definitions(
    assets = assets,
    schedules=schedules,
    jobs=jobs
)