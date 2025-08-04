#!/usr/bin/env bash

# Exit on error
set -o errexit

# Install Python dependencies (Render does this, but it's good for clarity)
pip install -r requirements.txt

python manage.py migrate  # Run database migrations
python manage.py collectstatic --noinput  # Collect static files
python manage.py seed  # Seed the database with a couple of emails and users
