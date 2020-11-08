"""Module with Point class implementation"""

from typing import Type
from math import hypot


class Point:
    """Point class implementation
    Usage: point = Point(numeric=0, numeric=0)"""

    # __slots__ = ['_x', '_y']

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """The initializer

        keyword arguments:
        -- x: x coord (numeric)
        -- y: y coord (numeric)"""

        self._x = float(x)
        self._y = float(y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Type) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Type) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return not self == other

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: float) -> float:
        self._x = float(value)

    @y.setter
    def y(self, value: float) -> float:
        self._y = float(value)

    def distance(self, other: Type) -> float:
        """Calculates distance between two points

        :param other: point object
        :type other: Point
        :returns: distance between two points
        :rtype: double
        :raises: TypeError"""

        if not isinstance(other, self.__class__):
            raise TypeError()
        return hypot(self.x - other.x, self.y - other.y)


if __name__ == '__main__':  # pragma: no cover
    p1 = Point()
    p2 = Point()
    p3 = Point(2, 7)

    if p1 == p2:
        print(f'{p1} == {p2}')

    if p1 != p3:
        print(f'{p1} != {p3}')

    p1.x = 10
    print(p1.x)
