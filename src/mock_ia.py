from src.types import MessageModel

def ia_response(input_text: str) -> MessageModel:
    user_message = input_text.lower()

    if "hello" in user_message:
        return MessageModel(role="assistant", content="Hello! How can I assist you today?")
    elif "help" in user_message:
        return MessageModel(role="assistant", content="Sure! What do you need help with?")
    else:
        return MessageModel(role="assistant", content="I'm sorry, I didn't understand that. Could you please rephrase?")
    