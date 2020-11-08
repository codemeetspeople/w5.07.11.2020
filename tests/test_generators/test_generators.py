import pytest
from generators import xrange


@pytest.mark.parametrize(
    'xrange_args, expected',
    [
        ((4,), (0, 1, 2, 3)),
        ((5, 10), (5, 6, 7, 8, 9)),
        ((5, 10, 2), (5, 7, 9)),
        ((10, 0, -2), (10, 8, 6, 4, 2))
    ]
)
def test_xrange(xrange_args, expected):
    generator = xrange(*xrange_args)

    for value in expected:
        assert next(generator) == value

    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize(
    'xrange_args, exception_type',
    [
        ((), TypeError),
        ((0, 10, -2), ValueError),
        ((10, 0, 2), ValueError),
        ((1, 10, 0), ValueError),
    ]
)
def test_xrange_exceptions(xrange_args, exception_type):
    with pytest.raises(exception_type):
        generator = xrange(*xrange_args)
        next(generator)
