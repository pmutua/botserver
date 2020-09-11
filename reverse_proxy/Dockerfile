FROM nginx:alpine
LABEL version="v0.0.0"
LABEL maintainer="philip@nouveta.tech"

RUN rm -rf /usr/share/nginx/html/*

COPY  ./default.conf  /etc/nginx/conf.d/default.conf

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static




