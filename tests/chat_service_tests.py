import pytest
from src.chat import post_message, get_chat_history, initialize_event_bus
from src.types import MessageModel


@pytest.mark.asyncio
async def test_post_message_stores_history():
    """Test that messages are stored in chat history."""
    user_msg = MessageModel(role="user", content="hello")
    
    result = await post_message(user_msg)
    
    # Should have user message + AI response
    assert len(result.chat) == 2
    assert result.chat[0].role == "user"
    assert result.chat[0].content == "hello"
    assert result.chat[1].role == "assistant"


@pytest.mark.asyncio
async def test_chat_history_accumulates():
    """Test that chat history accumulates over multiple messages."""
    await post_message(MessageModel(role="user", content="hello"))
    await post_message(MessageModel(role="user", content="help"))
    
    history = await get_chat_history()
    
    # Should have 4 messages (2 user + 2 AI)
    assert len(history.chat) == 4


@pytest.mark.asyncio
async def test_ai_response_triggered():
    """Test that AI response is triggered by user message."""
    user_msg = MessageModel(role="user", content="hello")
    
    result = await post_message(user_msg)
    
    # Check AI responded
    ai_message = result.chat[1]
    assert ai_message.role == "assistant"
    assert "Hello!" in ai_message.content