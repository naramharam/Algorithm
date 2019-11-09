class SubscriberOne(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{0}, {1}'.format(self.name, message))


class SubscriberTwo(object):
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print('{0}, {1}'.format(self.name, message))


class Publisher(object):
    def __init__(self):
        self.subscribers = dict()

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)


if __name__ == '__main__':
    pub = Publisher()

    astin = SubscriberOne('아스틴')
    james = SubscriberTwo('제임스')
    jeff = SubscriberOne('제')