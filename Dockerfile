# Use the official Python image as the base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies needed for psycopg2 (PostgreSQL adapter)
# and gunicorn/daphne to run your app.
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install Python dependencies
# This is separated to leverage Docker layer caching (faster rebuilds if code changes but requirements don't)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project code into the container
COPY . .

# Expose the port the Daphne server will listen on
EXPOSE 8000

# The final command to run the server is defined in docker-compose.yml
