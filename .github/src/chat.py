from bus.event_bus import EventBus
from src.types import MessageModel
from src.mock_ia import ia_response


def suscribe(message: MessageModel):
   pass    


def post_message(message: MessageModel) -> any:
    event_bus = EventBus()
    # suscribe the message event
    event_bus.subscribe(MessageModel, ia_response)
    event_bus.publish(MessageModel(role=message.role, content=message.content))
    # publish the message event    
    return message