#!/usr/bin/env bash
# Exit on any error
set -e

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
