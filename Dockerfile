FROM python:3.8-alpine

LABEL maintainer="TomaszDBogacki@gmail.com"
LABEL description="This is a Python3.8 container for med-files-api app"

ENV PYTHONUNBUFFERED 1
RUN apk add  --update --no-cache postgresql-client jpeg-dev
RUN apk add  --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps
ADD ./ /code/

RUN mkdir -p /vol/web/media
RUN mkdir - p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
