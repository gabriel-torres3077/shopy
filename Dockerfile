FROM python:3.10.3
LABEL maintaner="atorres.gabriel@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./shopy /shopy

WORKDIR /shopy
EXPOSE 8000

RUN pip install --upgrade pip && \
    apt update && apt -y install postgresql-client && \
    pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home shopy

USER shopy