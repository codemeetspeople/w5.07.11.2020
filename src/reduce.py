from functools import reduce

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum2(x, y):
    return x + y


def mult(x, y):
    return x * y


def handler(func, array):
    result = array[0]

    for item in array[1:]:
        result = func(result, item)
    return result


print(array)
print(handler(sum2, array))
print(handler(mult, array))
print('==================')

print(array)
print(handler(lambda x, y: x + y, array))
print(handler(lambda x, y: x * y, array))
print('==================')

print(array)
print(reduce(lambda x, y: x + y, array))
print(reduce(lambda x, y: x * y, array))
print('==================')
