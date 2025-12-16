# taken from https://www.youtube.com/watch?v=lCiW3BaOP04
from src.types import MessageModel

def ia_response(input_text: MessageModel) -> MessageModel:
    """Mock IA responses

    Args:
        input_text (MessageModel): input user message when post

    Returns:
        MessageModel: AI response message
    """
    user_message = input_text.content.lower()

    if "hello" in user_message:
        return MessageModel(role="assistant", content="Hello! How can I assist you today?")
    elif "help" in user_message:
        return MessageModel(role="assistant", content="Sure! What do you need help with?")
    else:
        return MessageModel(role="assistant", content="I'm sorry, I didn't understand that. Could you please rephrase?")
    