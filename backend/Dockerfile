FROM python:3.8.2

ENV DJANGO_SETTINGS_MODULE=backend.settings.production

WORKDIR /app
ADD . /app

RUN /app/setup_container.sh