#!/usr/bin/env sh
set -e

# Start the Python ML service (uvicorn) in background, then start the Node server in foreground.

cd "$(dirname "$0")/ml-service"

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    . .venv/bin/activate
elif [ -d "venv" ]; then
    . venv/bin/activate
fi

uvicorn main:app --host 0.0.0.0 --port 8000 &

cd "$(dirname "$0")"
exec node server/server.js
