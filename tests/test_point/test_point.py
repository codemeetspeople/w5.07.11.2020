import pytest

from point.point import Point


def test_point_constructor():
    point = Point()
    assert point.x == 0.0
    assert point.y == 0.0

    point = Point(1, 3)
    assert point.x == 1.0
    assert point.y == 3.0


def test_point_setters():
    point = Point()
    point.x = 42
    point.y = 42

    assert point.x == 42.0
    assert point.y == 42.0


def test_point_operators():
    p1 = Point()
    p2 = Point(1, 10)

    assert p1 != p2
    assert not p1 == p2


def test_point_distance():
    p1 = Point()
    p2 = Point(2, 4)

    assert p1.distance(p2) == 4.47213595499958


def test_point_representation():
    p1 = Point()
    str_point = '(0.0, 0.0)'

    assert str(p1) == str_point
    assert repr(p1) == str_point


def test_point_exception():
    with pytest.raises(TypeError):
        p1 = Point()
        p1.distance(dir)


def test_point_not_implemented():
    class Test:
        pass

    test = Test()
    p1 = Point()

    assert p1.__eq__(test) == NotImplemented
    assert p1.__ne__(test) == NotImplemented
