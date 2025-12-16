from bus.event_bus import EventBus
from src.types import ChatModel, MessageModel
from src.mock_ia import ia_response


# Create single instances to be reused
_event_bus = EventBus()
messages = []

# copilot suggested to initialize here in order to get IA responses before handling messages
# with this change is better to call this function once on application startup
# and not on every message post
def initialize_event_bus():
    """
    Initialize the event bus with AI response handler.
    This separates setup from message handling.
    Call this once on application startup.
    """
    # Subscribe AI to respond to user messages
    _event_bus.subscribe(MessageModel, ia_response) 


async def post_message(message: MessageModel) -> ChatModel:
   """
   Handle incoming user message using event-driven architecture:
   1. Store user message
   2. Publish user message to event bus
   3. AI handler responds via event bus
   4. Store AI response
   5. Return complete chat history

   Args:
      message: User's message
      
   Returns:
      ChatModel containing full chat history
   """
   # Store user message
   messages.append(message)

   # Publish to event bus - AI will respond
   responses = _event_bus.publish(message)

   # Store AI responses (should be 1 response from ia_response handler)
   for response in responses:
      if isinstance(response, MessageModel):
            messages.append(response)

   # Return full chat history
   return ChatModel(chat=messages)


async def get_chat_history() -> ChatModel:
    """
    Retrieve complete chat history.
    
    Returns:
        ChatModel containing all messages
    """
    return ChatModel(chat=messages)