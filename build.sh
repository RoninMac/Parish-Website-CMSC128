#!/usr/bin/env bash
set -o errexit

echo "DATABASE_URL is set: $DATABASE_URL"
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate