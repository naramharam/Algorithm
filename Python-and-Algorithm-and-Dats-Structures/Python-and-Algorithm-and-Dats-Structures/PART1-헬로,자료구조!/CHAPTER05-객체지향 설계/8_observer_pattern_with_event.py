class Publisher(object):

    def __init__(self, events):
        self.subscribers = {events:dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)