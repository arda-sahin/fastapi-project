#!/bin/sh


echo "Waiting for database at $DB_HOST:$DB_PORT..."

# Wait for the database to be ready:
#nc -z $DB_HOST $DB_PORT → Tests the connection to the DB port with netcat.
#sleep 1 → Waits 1 second between each attempt.
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "Database running! Starting the application..."

# Start the application with Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 80
