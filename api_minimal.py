#!/usr/bin/env python3
"""
Minimal Backend Server for AgenticSeek
This is a simplified version that can run without all heavy ML dependencies.
For production use, use api.py with full dependencies installed.
"""

import os
import sys
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="AgenticSeek API (Minimal)",
    version="0.1.0",
    description="Minimal backend server for testing and development"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    done: str
    answer: str
    reasoning: str = ""
    agent_name: str = "MinimalAgent"
    success: str = "true"
    blocks: dict = {}
    status: str = "Ready"
    uid: str = ""

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify the server is running."""
    return {
        "status": "healthy",
        "version": "0.1.0-minimal",
        "message": "Minimal backend server is running"
    }

# Check if agent is active
@app.get("/is_active")
async def is_active():
    """Check if the agent is currently processing a request."""
    return {"is_active": False}

# Stop endpoint
@app.get("/stop")
async def stop():
    """Stop the current agent processing."""
    return JSONResponse(
        status_code=200,
        content={"status": "stopped", "message": "No active processing to stop"}
    )

# Latest answer endpoint
@app.get("/latest_answer")
async def get_latest_answer():
    """Get the latest answer from the agent."""
    return JSONResponse(
        status_code=404,
        content={"error": "No answer available in minimal mode"}
    )

# Process query endpoint
@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Process a query. This minimal version returns a mock response.
    For full functionality, use api.py with all dependencies installed.
    """
    print(f"[Minimal Server] Received query: {request.query}")
    
    response = QueryResponse(
        done="true",
        answer=f"Minimal server received your query: '{request.query}'. "
                "This is a simplified backend for testing. "
                "For full functionality, please use the complete api.py with all dependencies.",
        reasoning="Minimal server mode - returning mock response",
        agent_name="MinimalAgent",
        success="true",
        blocks={},
        status="Complete",
        uid="minimal-" + str(hash(request.query))
    )
    
    return JSONResponse(
        status_code=200,
        content=response.model_dump()
    )

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with server information."""
    return {
        "name": "AgenticSeek Minimal Backend",
        "version": "0.1.0",
        "status": "running",
        "message": "This is a minimal version for testing. Use api.py for full features.",
        "endpoints": {
            "health": "/health",
            "query": "/query (POST)",
            "is_active": "/is_active",
            "stop": "/stop",
            "latest_answer": "/latest_answer"
        }
    }

if __name__ == "__main__":
    # Get port from environment or default to 7777
    port = int(os.getenv("BACKEND_PORT", "7777"))
    
    print("=" * 70)
    print(f"Starting AgenticSeek Minimal Backend Server")
    print(f"Version: 0.1.0-minimal")
    print(f"Port: {port}")
    print(f"Health check: http://localhost:{port}/health")
    print(f"API docs: http://localhost:{port}/docs")
    print("=" * 70)
    
    # Run the server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
