FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libc-dev \
    libpq-dev \
    libproj-dev \
    proj-data \
    proj-bin \
    libgeos-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app
