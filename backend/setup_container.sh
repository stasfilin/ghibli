#!/usr/bin/env bash

apt-get update && apt-get install -y \
    python3-pip postgresql-client postgresql-contrib

pip install --upgrade pip setuptools wheel pipenv==2018.11.26
pipenv install --dev --system --deploy
chmod +x /app/runserver.sh