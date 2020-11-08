from string import ascii_lowercase
from random import choice

from zoo.settings import ANIMALS_PATH


def deliver(animal):
    TEMPLATE = (
        '\n\n@animal_in_zoo\n'
        'class {animal_cls}(Animal):\n'
        '    @classmethod\n'
        '    def speak(cls):\n'
        '        print(f\'{{cls.get_title()}} say {sound}-{sound}\')\n'
    )

    sound = ''.join([choice(ascii_lowercase) for _ in range(4)])

    animal_class = TEMPLATE.format(
        animal_cls=animal.capitalize(),
        sound=sound
    )

    with open(ANIMALS_PATH, 'r') as file:
        source = file.read()

    final_code = f'{source}{animal_class}'

    with open(ANIMALS_PATH, 'w') as file:
        source = file.write(final_code)
