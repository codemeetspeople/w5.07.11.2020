__all__ = (
    'Integer',
    'Float',
    'AbsoluteMixin',
    'SquareMixin',
    'AbsoluteInteger',
    'AbsoluteFloat',
    'SquareInteger',
    'SquareFloat',
)


class Number:
    _validator = None

    def __init__(self, value):
        self._value = self._validator(value)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)


class Integer(Number):
    _validator = int

    def __init__(self, value):
        super().__init__(value)


class Float(Number):
    _validator = float

    def __init__(self, value):
        super().__init__(value)


class AbsoluteMixin:
    @property
    def absolute(self):
        return self.value * -1 if self.value < 0 else self.value


class SquareMixin:
    @property
    def square(self):
        return self.value ** 2


class AbsoluteInteger(Integer, AbsoluteMixin):
    pass


class AbsoluteFloat(Float, AbsoluteMixin):
    pass


class SquareInteger(Integer, SquareMixin):
    pass


class SquareFloat(Float, SquareMixin):
    pass
