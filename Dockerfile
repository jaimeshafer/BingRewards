FROM chainguard/python:latest-dev AS builder
USER root
WORKDIR /app

ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

COPY pyproject.toml poetry.lock* ./

RUN python -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

RUN pip install --no-cache-dir poetry \
    && poetry install --no-root --only main


FROM chainguard/python:latest

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DAGSTER_HOME=/app/dagster_home
ENV PATH="/app/.venv/bin:$PATH"

COPY --from=builder /app/.venv /app/.venv
COPY . .

EXPOSE 30303

ENTRYPOINT ["/app/.venv/bin/python"]
CMD ["-m", "dagster", "dev", "-m", "dags.definitions", "-h", "0.0.0.0", "-p", "30303"]