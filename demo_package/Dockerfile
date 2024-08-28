FROM python:3.11-slim AS base

ARG POETRY_HOME=/etc/poetry
ENV PATH="${PATH}:${POETRY_HOME}/bin"
WORKDIR /root/package

RUN apt update && \
    apt install -y curl && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python - --version 1.8.2 && \
    poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction

COPY ./README.md ./
COPY ./demo_package ./demo_package

CMD [ "poetry", "build" ]

