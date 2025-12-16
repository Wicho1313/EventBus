from fastapi import FastAPI, HTTPException
from src import types
from src.chat import initialize_event_bus, post_message as post_message_handler
from src.chat import get_chat_history as history_handler

app = FastAPI(title="Event-Driven Chat Service")


# Copilot suggested to add startup event to initialize event bus
# so that we don't have to do it on every message post
@app.on_event("startup")
async def startup_event():
    """Initialize event bus with AI subscriber on application startup."""
    initialize_event_bus()


@app.post("/post_message", response_model=types.ChatModel, response_model_by_alias=True)
async def post_message_endpoint(message: types.MessageModel):
    """
    Post a user message to the chat.
    Returns complete chat history including AI response.
    """
    try:
        return await post_message_handler(message) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/chat_history", response_model=types.ChatModel, response_model_by_alias=True)
async def get_history():
    """
    Retrieve complete chat history.
    """
    try:
        return await history_handler()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check() -> str:
    """Health check endpoint."""
    return "OK"