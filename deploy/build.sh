#!/bin/bash

# Upgrade Resources
pip install --upgrade pip
pip install uv

# Install dependencies
echo "Installing dependencies..."
source "${VENV_ROOT}/bin/activate"
uv sync

# Apply database migrations
echo "Applying database migrations..."
uv run manage.py migrate --noinput

# Run Tailwind setup
echo "Running Tailwind setup..."
uv run manage.py tailwind setup

# Run Tailwind build
echo "Running Tailwind build..."
uv run manage.py tailwind build

# Collect static files
echo "Collecting static files..."
uv run manage.py collectstatic --noinput