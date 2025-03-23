FROM python:3.11-slim

ENV TZ Europe/London
ARG STAGE=prod
ENV STAGE=${STAGE} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PATH=$PATH:/root/.local/bin:/root/.poetry/bin

RUN apt update -qq && \
    apt install curl build-essential -y -qq > /dev/null && \
    apt clean -y && \
    pip3 install -U -q poetry

WORKDIR /app
COPY poetry.lock pyproject.toml run.sh ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root --no-ansi $(test "${STAGE}" != local && echo "--only main")


COPY . /app/

CMD ["./entrypoint.sh"]

