from bus.event_bus import EventBus
from src.types import MessageModel


def test_event_bus_singleton():
    """Test that EventBus is a singleton."""
    bus1 = EventBus()
    bus2 = EventBus()
    assert bus1 is bus2


def test_subscribe_and_publish():
    """Test basic pub/sub functionality."""
    bus = EventBus()
    
    received_events = []
    
    def handler(event: MessageModel) -> MessageModel:
        received_events.append(event)
        return MessageModel(role="assistant", content="Response")
    
    bus.subscribe(MessageModel, handler)
    
    test_message = MessageModel(role="user", content="Test")
    responses = bus.publish(test_message)
    
    assert len(received_events) == 1
    assert received_events[0].content == "Test"
    assert len(responses) == 1
    assert responses[0].content == "Response"


def test_multiple_subscribers():
    """Test multiple handlers for same event type."""
    bus = EventBus()
    
    call_count = [0]
    
    def handler1(event: MessageModel):
        call_count[0] += 1
    
    def handler2(event: MessageModel):
        call_count[0] += 1
    
    bus.subscribe(MessageModel, handler1)
    bus.subscribe(MessageModel, handler2)
    
    bus.publish(MessageModel(role="user", content="Test"))
    
    assert call_count[0] == 2