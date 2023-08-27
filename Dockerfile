FROM python:3.10.12-slim-bookworm@sha256:13cc673c11ee90d6ba92d95f35f4d8e59148937f1e3b4044788e93268bfe9d2e

ENV TZ="America/Sao_Paulo"
ENV FLASK_ENV=development

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get install -y netcat-openbsd \
    && chmod 777 entrypoint.sh \
    && apt-get install --no-install-recommends -y python3-pip \
    && pip3 install -r requirements.txt \
    && apt-get clean