class Symbol(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented


if __name__ == '__main__':
    x = Symbol('Py')
    y = Symbol('Py')

    Symbol = set()
    Symbol.add(x)
    Symbol.add(y)

    print(x is y)
    print(x == y)
    print(len(Symbol))