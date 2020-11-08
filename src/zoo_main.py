from importlib import reload

from zoo import animals
from zoo.delivery import deliver


def main():
    while True:
        animals_list = ', '.join(animals.ANIMALS.keys())
        print(f'Available animals: {animals_list}')

        action = input().strip().lower()

        if action == 'exit':
            print('Bye-bye')
            exit()

        if action in animals.ANIMALS:
            animals.ANIMALS[action].speak()
        else:
            print(f'{action} is not available!')
            deliver(action)
            reload(animals)

        print('================')
        print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Bye-bye')
