#!/bin/bash
echo "BUILD START"
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

echo "BUILD END"
