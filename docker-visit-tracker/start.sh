#!/bin/sh

echo "Waiting for MySQL to be available..."

while ! nc -z $DB_HOST 3306; do
  echo "Waiting for MySQL at $DB_HOST:3306..."
  sleep 2
done

echo "MySQL is up — launching app"
exec uvicorn app:app --host 0.0.0.0 --port 8080
