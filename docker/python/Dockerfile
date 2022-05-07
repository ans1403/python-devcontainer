FROM python:3.10.4-bullseye

WORKDIR /usr/local/python-devcontainer

COPY ./requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        gcc \
    \
    && pip install --no-cache-dir -r ./requirements.txt \
    && pip install --no-cache-dir \
        black \
        flake8 \
    \
    && apt-get autoremove -y \
    && apt-get clean -y
