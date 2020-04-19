FROM python:3.8-alpine

LABEL maintainer="TomaszDBogacki@gmail.com"
LABEL description="This is a Python3.8 container for med-files-api app"

ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./ /code/
