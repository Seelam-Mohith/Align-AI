#!/bin/bash
# start-all.sh - Unix/macOS script to start all services

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo "========================================"
echo " AI Career Assistant - Starting Services"
echo "========================================"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "[ERROR] Node.js is not installed"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python is not installed"
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

echo "[OK] Node.js found: $(node --version)"
echo "[OK] Python found: $(python3 --version)"
echo ""

# Function to start backend
start_backend() {
    echo "Starting Backend (Express.js on port 5000)..."
    cd "$SCRIPT_DIR/server"
    npm install --silent
    npm run dev
}

# Function to start ML service
start_ml_service() {
    echo "Starting ML Service (FastAPI on port 8000)..."
    cd "$SCRIPT_DIR/ml-service"
    
    # Create and activate virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    pip install -q -r requirements.txt
    python3 main.py
}

# Function to start frontend
start_frontend() {
    echo "Starting Frontend (React on port 3000)..."
    cd "$SCRIPT_DIR/client"
    npm install --silent
    npm start
}

# Start all services in background
start_backend &
BACKEND_PID=$!

sleep 3

start_ml_service &
ML_PID=$!

sleep 3

start_frontend &
FRONTEND_PID=$!

echo ""
echo "========================================"
echo " Services Starting..."
echo "========================================"
echo ""
echo "Frontend:   http://localhost:3000"
echo "Backend:    http://localhost:5000"
echo "ML Service: http://localhost:8000"
echo ""
echo "All services should be ready in 30-60 seconds"
echo "Press Ctrl+C to stop all services"
echo ""

# Trap Ctrl+C to stop all processes
trap "kill $BACKEND_PID $ML_PID $FRONTEND_PID; echo 'Services stopped'; exit 0" INT

# Wait for all processes
wait
