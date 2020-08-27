# pull official base image
FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"


COPY ./requirements.txt .


COPY ./env .


# install psycopg2 dependencies no cache to keep it light weight
RUN apk add --update --no-cache --virtual .tmp  postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip


RUN pip install -r requirements.txt

# remove dependencies 

RUN apk del .tmp

RUN mkdir /app

COPY ./app /app

WORKDIR /app

COPY ./scripts /scripts

RUN chmod +x  /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user 

RUN chown -R user:user /vol

RUN chmod -R 755 /vol/web

USER user

CMD ["entrypoint.sh"]
