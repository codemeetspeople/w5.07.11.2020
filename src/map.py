array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def increment(x):
    return x + 1


def power(x):
    return x ** 2


def sequence_handler(func, sequence):
    result = []

    for elem in sequence:
        result.append(func(elem))

    return result


print(array)
print(sequence_handler(increment, array))
print(sequence_handler(power, array))
print('===============')

print(array)
print(sequence_handler(lambda x: x + 1, array))
print(sequence_handler(lambda x: x ** 2, array))
print('===============')

print(array)
print(list(map(lambda x: x + 1, array)))
print(list(map(lambda x: x ** 2, array)))
print('===============')
