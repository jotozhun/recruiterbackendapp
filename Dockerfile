FROM python:3.10.9-alpine3.17
LABEL MAINTAINER="Jopoelpe"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./recruiterapp /recruiterapp
WORKDIR /recruiterapp
EXPOSE 8000

ARG DEV=false
RUN python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV == 'true' ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home  \
        dev-user

ENV PATH="/py/bin:$PATH"
USER dev-user