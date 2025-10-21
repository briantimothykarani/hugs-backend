# Use the official Python 3.11 Alpine image
FROM python:3.11-alpine

# Environment variables to prevent .pyc files and enable live output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    build-base

# Set work directory
WORKDIR /usr/src/app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port Daphne will run on
EXPOSE 8000

