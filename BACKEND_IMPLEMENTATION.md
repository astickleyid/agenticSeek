# Backend Server Implementation

This document describes the implementation and usage of the AgenticSeek backend server.

## Overview

The backend server has been implemented and is now running successfully. Two versions are available:

1. **api_minimal.py** - A minimal version for testing and development with reduced dependencies
2. **api.py** - The full-featured version with all ML capabilities (requires all dependencies)

## Minimal Backend Server

### Purpose

The minimal backend server (`api_minimal.py`) provides:
- Core FastAPI endpoints compatible with the frontend
- Minimal dependencies (only FastAPI, Uvicorn, Pydantic, python-dotenv)
- Quick startup for testing and CI/CD environments
- Mock responses for all endpoints

### Running the Minimal Server

```bash
# Install minimal dependencies
pip install fastapi uvicorn pydantic python-dotenv aiofiles celery redis

# Create .env file
cp .env.example .env

# Start the server
python3 api_minimal.py
```

The server will start on port 7777 by default (configurable via `BACKEND_PORT` environment variable).

### Available Endpoints

- `GET /` - Server information and available endpoints
- `GET /health` - Health check endpoint
- `GET /is_active` - Check if agent is processing
- `GET /stop` - Stop current processing
- `GET /latest_answer` - Get latest response
- `POST /query` - Process a query (returns mock response)

### Testing the Server

```bash
# Health check
curl http://localhost:7777/health

# Get server info
curl http://localhost:7777/

# Test query endpoint
curl -X POST http://localhost:7777/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello, can you help me?"}'
```

## Full Backend Server

### Prerequisites

For the full backend server (`api.py`), you need:
- Python 3.10.x (recommended)
- All dependencies from `requirements.txt`
- Chrome/Chromedriver for browser automation
- Optional: Local LLM provider (Ollama, LM Studio, etc.)

### Running with Docker

```bash
# Create .env file
cp .env.example .env
# Edit .env with your settings

# Start all services including backend
./start_services.sh full
```

### Running on Host

```bash
# Install all dependencies
pip install -r requirements.txt

# Create .env file and configure
cp .env.example .env

# Update SEARXNG_BASE_URL in .env to http://localhost:8080 for host mode

# Start required services (SearxNG, Redis)
./start_services.sh

# Start the backend
python3 api.py
```

## Configuration

### Environment Variables (.env)

```env
SEARXNG_BASE_URL="http://searxng:8080"  # or http://localhost:8080 for host mode
REDIS_BASE_URL="redis://redis:6379/0"
WORK_DIR="/path/to/workspace"
BACKEND_PORT="7777"
OLLAMA_PORT="11434"
LM_STUDIO_PORT="1234"
```

### Config File (config.ini)

```ini
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:14b
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis
recover_last_session = False
save_session = False
speak = False
listen = False
jarvis_personality = False
languages = en

[BROWSER]
headless_browser = True
stealth_mode = False
```

## Status

✅ Minimal backend server implemented and running
✅ All required endpoints available
✅ Health check endpoint responding
✅ Query endpoint accepting and processing requests
✅ CORS configured for frontend integration
✅ Environment configuration via .env file

## Next Steps

For production use:
1. Install full dependencies from requirements.txt
2. Set up local LLM provider (Ollama recommended)
3. Configure config.ini with your provider settings
4. Use api.py instead of api_minimal.py

## Troubleshooting

### Port Already in Use

If port 7777 is in use, either:
- Set `BACKEND_PORT` environment variable to a different port
- Kill the process using the port: `lsof -ti:7777 | xargs kill -9`

### Docker Build Issues

If Docker build fails (e.g., Chrome download issues):
- Run the backend on the host instead
- Check network connectivity
- See ChromeDriver section in main README.md

### Disk Space Issues

If pip install fails with "No space left on device":
```bash
# Clean pip cache
pip cache purge

# Clean Docker
docker system prune -af --volumes
```
