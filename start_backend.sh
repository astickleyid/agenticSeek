#!/bin/bash
# Startup script for AgenticSeek minimal backend server

set -e

echo "======================================================================"
echo "Starting AgenticSeek Minimal Backend Server"
echo "======================================================================"

# Check if .env exists
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "Please edit .env with your settings before running in production"
fi

# Check if required Python packages are installed
echo "Checking dependencies..."
python3 -c "import fastapi, uvicorn, pydantic" 2>/dev/null || {
    echo "Installing minimal dependencies..."
    pip3 install fastapi uvicorn pydantic python-dotenv aiofiles
}

# Get port from environment or use default
PORT=${BACKEND_PORT:-7777}

# Check if port is already in use
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "Warning: Port $PORT is already in use"
    read -p "Do you want to kill the process and continue? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Killing process on port $PORT..."
        lsof -ti:$PORT | xargs kill -9
        sleep 2
    else
        echo "Exiting. Please free port $PORT or set BACKEND_PORT to a different port"
        exit 1
    fi
fi

echo ""
echo "Starting server on port $PORT..."
echo "Health check: http://localhost:$PORT/health"
echo "API docs: http://localhost:$PORT/docs"
echo "Press Ctrl+C to stop"
echo "======================================================================"
echo ""

# Start the server
python3 api_minimal.py
