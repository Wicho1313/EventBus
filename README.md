# EventBus - Event-Driven Chat Service

-- this documentation was made with AI help --

Minimal event-driven chat service demonstrating pub/sub architecture with a mock AI assistant.

## Architecture

```
Client → FastAPI → ChatService → EventBus → AI Agent
                       ↓            ↓         ↓
                   ChatStore    Publish   Subscribe
                       ↓            ↓         ↓
                   Response  ←  Event   ←  Response
```

**Key Components:**
- **EventBus**: Singleton pub/sub broker (decouples components)
- **ChatService**: REST API endpoints
- **ChatStore**: In-memory message persistence
- **AI Agent**: Mock AI that subscribes to user messages

## Setup

```bash
# Install dependencies
pip install fastapi uvicorn pydantic pytest pytest-asyncio

# Run server
python -m uvicorn services.chat_service:app --reload

# Or use VS Code debugger (F5)
```

## API Endpoints

**POST /post_message**
```json
{
  "role": "user",
  "content": "hello"
}
```

**GET /chat_history**

**GET /health**

## Testing

```bash
pytest tests/
```

## Event Flow

1. User sends message → POST /post_message
2. Message stored in ChatStore
3. Message published to EventBus
4. AI handler receives event, generates response
5. AI response stored in ChatStore
6. Complete chat history returned to client# EventBus
Minimal event-driven chat service
