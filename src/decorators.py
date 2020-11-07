def run_X_times(x):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for i in range(x):
                func(*args, **kwargs)
        inner_wrapper.__name__ = func.__name__
        return inner_wrapper
    return outer_wrapper


def print_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        func(*args, **kwargs)
    return wrapper


@print_name
@run_X_times(2)
def hello(user):
    print(f'hello, {user}')


@print_name
@run_X_times(4)
def my_sum(x, y):
    print(f'{x} + {y} = {x+y}')


hello('caiman')
my_sum(5, 10)
