class Animal:
    def eat(self):
        print(f'{self.__class__.__name__} eats everything...')

    def make_sound(self):
        print(f'{self.__class__.__name__} say ololo...')


class Dog(Animal):
    def bark(self):
        print(f'{self.__class__.__name__} say grrr...')

    def eat(self):
        print(f'{self.__class__.__name__} eats meat...')


class Cat(Animal):
    def meow(self):
        print(f'{self.__class__.__name__} say meow...')

    def eat(self):
        print(f'{self.__class__.__name__} eats fish...')


class CatDog(Dog, Cat):
    def speak(self):
        print(f'{self.__class__.__name__} say "Hello"')

    def eat(self):
        print(f'{self.__class__.__name__} eats meat and fish...')


if __name__ == "__main__":
    cd = CatDog()
    cd.bark()
    cd.meow()
    cd.make_sound()
    cd.eat()

    super(CatDog, cd).eat()  # parent method call
