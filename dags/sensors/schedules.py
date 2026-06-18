from dagster import ScheduleDefinition, DefaultScheduleStatus
from dags.jobs import *

daily_job_schedule = ScheduleDefinition(
    job=daily_job,
    cron_schedule="0 3 * * *",
    execution_timezone="America/CHicago",
    default_status=DefaultScheduleStatus.RUNNING,
)

schedules = [
    daily_job_schedule,
]