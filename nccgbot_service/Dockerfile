# pull official base image
FROM python:3.8.0-slim


LABEL version="v1.0.0"
LABEL maintainer="philip@nouveta.tech"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"


RUN mkdir /app


WORKDIR /app

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .


RUN pip install -r requirements.txt

COPY . .

COPY  ./entrypoint.sh .


RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static


RUN adduser --disabled-password --gecos '' user 


# RUN chown -R user:user /

RUN chown -R 755 /vol/web

# USER user




