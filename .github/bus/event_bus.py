# took from: https://www.youtube.com/watch?v=tJIHxUYHDW4

class EventBus:
    """
    event bus to suscribe and publish events
    """
    def __init__(self):
        self.suscribers = {}

    def publish(self, event):
        if event.__class__ not in self.suscribers:
            return
        
        for callback in self.suscribers[event.__class__]:   
            callback(event)

    def subscribe(self, event_class, callback):
        if event_class not in self.suscribers:
            self.suscribers[event_class] = [callback]
            return
        
        self.suscribers[event_class].append(callback)