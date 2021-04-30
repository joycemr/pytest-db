#pull official base image
FROM python:3.8.1-alpine

# set work directory
WORKDIR /src

# copy requirements file
COPY ../test/requirements.txt /src/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /src/requirements.txt \
    && rm -rf /root/.cache/pip

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTEST_ADDOPTS="--color=yes"
ENV SQL_UNIT_TEST_TEMPLATE_DB_URL=postgresql://postgres:postgres@host.docker.internal:5432/postgres

WORKDIR /test

CMD ["pytest"]
