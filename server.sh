#!/bin/bash

set -e

export DJANGO_SETTINGS_MODULE=knowflow.settings

if [ "$ENVIRONMENT" = "local" ]; then
    echo "Running local development server."
    exec python manage.py runserver "$BASE_URL"
else
    echo "Running gunicorn server."
    exec gunicorn knowflow.wsgi:application \
        --name knowflow \
        --bind "$BASE_URL" \
        --reload \
        --workers 2 \
        --log-level=debug \
        "$@"
fi
