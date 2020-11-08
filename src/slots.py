from pympler.asizeof import asizeof


class A:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class B:
    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


if __name__ == '__main__':
    dict_object = A()
    slot_object = B()

    print(f'Object with __dict__ property size: {asizeof(dict_object)}')
    print(f'Object with __slots__ property size: {asizeof(slot_object)}')
