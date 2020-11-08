import pytest

from mixins import (
    Integer,
    Float,
    AbsoluteInteger,
    AbsoluteFloat,
    SquareInteger,
    SquareFloat
)


@pytest.mark.parametrize(
    'obj_class, value, str_repr', [
        (Integer, 10, '10'),
        (Float, 10, '10.0'),
        (AbsoluteInteger, 10, '10'),
        (AbsoluteFloat, 10, '10.0'),
        (SquareInteger, 10, '10'),
        (SquareFloat, 10, '10.0'),
    ]
)
def test_constructor(obj_class, value, str_repr):
    object = obj_class(value)

    assert object.value == value
    assert str(object) == str_repr


@pytest.mark.parametrize(
    'obj_class, value, expected', [
        (AbsoluteInteger, -10, 10),
        (AbsoluteFloat, -10, 10),
    ]
)
def test_absolute_mixin(obj_class, value, expected):
    object = obj_class(value)

    assert object.absolute == expected


@pytest.mark.parametrize(
    'obj_class, value, expected', [
        (SquareInteger, 10, 100),
        (SquareFloat, 10, 100),
    ]
)
def test_square_mixin(obj_class, value, expected):
    object = obj_class(value)

    assert object.square == expected
