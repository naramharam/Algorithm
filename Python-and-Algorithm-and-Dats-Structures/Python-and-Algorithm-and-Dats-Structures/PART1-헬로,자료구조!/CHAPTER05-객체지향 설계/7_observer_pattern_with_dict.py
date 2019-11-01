class SubscriberOne(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{0}, {1}'.format(self.name, message))


class Publisher(object):
    def __init__(self, events):
        self.subscribers = {events:dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')s
        self.get_subscribers(event)[who] = callback

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)



if __name__ == '__main__':
    pub = Publisher(['점심', '퇴근'])

    astin = Subscriber('아스')