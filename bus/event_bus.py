# took from: https://www.youtube.com/watch?v=tJIHxUYHDW4

class EventBus:
    """
    event bus to suscribe and publish events
    """
    def __init__(self):
        self.suscribers = {}

    def publish(self, event):
        """
        Publish an event to all subscribers.
        Returns a list of responses from all callbacks.
        """
        if event.__class__ not in self.suscribers:
            return []
        # copilot suggested to return a list of responses
        responses = []
        for callback in self.suscribers[event.__class__]:   
            response = callback(event)
            if response is not None:
                responses.append(response)

        return responses

    def subscribe(self, event_class, callback):
        """Subscribe a callback function to an event type."""
        if event_class not in self.suscribers:
            self.suscribers[event_class] = [callback]
            return
        
        self.suscribers[event_class].append(callback)