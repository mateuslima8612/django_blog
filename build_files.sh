#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Make sure staticfiles directory exists
mkdir -p staticfiles

echo "Build completed successfully"