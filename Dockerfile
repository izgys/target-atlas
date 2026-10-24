# Target Atlas — container image.
#
#   docker build -t target-atlas .
#   docker run --rm -e ANTHROPIC_API_KEY -v "$(pwd)/results:/app/results" target-atlas run EGFR
#
# The API key is passed at runtime (-e or --env-file) and never copied into the
# image: .dockerignore keeps .env out of the build context.

FROM python:3.12-slim-bookworm

# uv binary only, pinned to the version that wrote uv.lock
COPY --from=ghcr.io/astral-sh/uv:0.11.12 /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    PATH="/app/.venv/bin:$PATH" \
    TARGET_ATLAS_CONFIG_DIR=/app/configs \
    MLFLOW_DISABLE_TELEMETRY=true \
    GIT_PYTHON_REFRESH=quiet
# GIT_PYTHON_REFRESH: MLflow looks for a git executable; the image has none

WORKDIR /app

# 1. Dependencies only. This layer is rebuilt only when pyproject.toml or
#    uv.lock change, so editing code does not reinstall everything.
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

# 2. The project itself
COPY src ./src
COPY configs ./configs
COPY evals ./evals
RUN uv sync --locked --no-dev

# 3. Run as an unprivileged user; it owns only the folders the program writes to
RUN useradd --create-home --uid 1000 atlas \
    && mkdir -p results evals/results evals/cache mlruns \
    && chown -R atlas:atlas results evals/results evals/cache mlruns
USER atlas

# Recorded in eval results when there is no .git inside the image:
#   docker build --build-arg GIT_COMMIT=$(git rev-parse --short HEAD) -t target-atlas .
# Declared last on purpose: a value that changes every commit would otherwise
# invalidate the cached dependency layer and force a full reinstall.
ARG GIT_COMMIT=unknown
ENV GIT_COMMIT=${GIT_COMMIT}

ENTRYPOINT ["target-atlas"]
CMD ["--help"]
