@echo off
REM Startup script for AgenticSeek minimal backend server (Windows)

echo ======================================================================
echo Starting AgenticSeek Minimal Backend Server
echo ======================================================================

REM Check if .env exists
if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo Please edit .env with your settings before running in production
)

REM Check if required Python packages are installed
echo Checking dependencies...
python -c "import fastapi, uvicorn, pydantic" 2>nul
if errorlevel 1 (
    echo Installing minimal dependencies...
    pip install fastapi uvicorn pydantic python-dotenv aiofiles
)

REM Get port from environment or use default
if not defined BACKEND_PORT set BACKEND_PORT=7777

echo.
echo Starting server on port %BACKEND_PORT%...
echo Health check: http://localhost:%BACKEND_PORT%/health
echo API docs: http://localhost:%BACKEND_PORT%/docs
echo Press Ctrl+C to stop
echo ======================================================================
echo.

REM Start the server
python api_minimal.py
