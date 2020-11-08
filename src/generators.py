def xrange(start=None, stop=None, step=1):
    if start is None:
        raise TypeError()

    if stop is None:
        start, stop = 0, start

    if step == 0:
        raise ValueError()

    if step < 0 and start <= stop:
        raise ValueError()

    if step > 0 and start >= stop:
        raise ValueError()

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


if __name__ == '__main__':  # pragma: no cover
    print('xrange(4)')
    for i in xrange(4):
        print(i)

    print('xrange(5, 10)')
    for i in xrange(5, 10):
        print(i)

    print('xrange(5, 10, 2)')
    for i in xrange(5, 10, 2):
        print(i)

    print('xrange(10, 0, -2)')
    for i in xrange(10, 0, -2):
        print(i)
