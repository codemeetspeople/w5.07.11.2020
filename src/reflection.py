class Integer:
    def __init__(self, value=0):
        self._value = int(value)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.value + other.value)
        return NotImplemented


class Float:
    def __init__(self, value=0):
        self._value = float(value)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        return NotImplemented


integer = Integer(10)
my_float = Float(5)

print(integer + my_float)
