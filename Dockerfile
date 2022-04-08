FROM python:3.9.12-alpine3.15

EXPOSE 8000

ENV \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYTHONDONTWRITEBYTECODE=1

RUN apk update
RUN apk add --no-cache busybox-extras bash \
    openssh jpeg-dev postgresql-dev \
    postgresql-dev gcc musl-dev \
    alpine-sdk libffi-dev libcurl curl-dev

RUN apk add --virtual .build-deps

RUN pip install -U pip && pip install poetry

WORKDIR /app


COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

CMD ["tail", "-f", "/dev/null"]