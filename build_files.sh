#!/bin/bash
echo "BUILD START"
# Install dependencies
pip install -r requirements.txt

# Run migrations


python manage.py migrate
python manage.py makemigrations

# Collect static files
python manage.py collectstatic --noinput

echo "BUILD END"
