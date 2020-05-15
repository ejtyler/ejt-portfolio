#!/bin/bash
echo "Running release tasks"

echo "Running database migrations"
python manage.py migrate

echo "Collecting static files"
python manage.py collectstatic

echo "Done running release tasks"
