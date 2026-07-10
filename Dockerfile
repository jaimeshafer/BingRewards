FROM chainguard/python:latest-dev AS builder
USER root

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
COPY . .

RUN apk add --no-cache coreutils

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir poetry \
    && poetry install --no-root --only main


ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/.venv/lib/python3.14/site-packages:/app" \
    DAGSTER_HOME=/app/dagster_home \
    TZ=America/Chicago \
    PYTHONUNBUFFERED=1


EXPOSE 30303

ENTRYPOINT ["/app/.venv/bin/dagster"]
CMD ["dev", "-w", "/app/workspace.yaml", "--host", "0.0.0.0", "--port", "30303"]