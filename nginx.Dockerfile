FROM nginx:latest

LABEL maintainer="Mr-Linus admin@run-linux.com"

ARG TZ="Asia/Shanghai"

ENV TZ ${TZ}

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY . /usr/share/nginx/html/Tower