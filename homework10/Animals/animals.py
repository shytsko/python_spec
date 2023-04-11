# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого кла.
from enum import Enum

__all__ = ["Cat", "Dog", "Fish", "Animal"]


class Animal:
    def __init__(self, species: str, name: str, age: str):
        self._species = species
        self._name = name
        self._age = age

    def __str__(self):
        return f"Это животное {self._species}, зовут {self._name}, возраст {self._age} лет"


class Cat(Animal):
    __species = "кот"
    def __init__(self, name: str, age: str, color: str):
        super().__init__(self.__species, name, age)
        self._color = color

    def __str__(self):
        return f"{super().__str__()}, цвет {self._color}"


class Dog(Animal):
    __species = "собака"
    def __init__(self, name: str, age: str, angry: bool):
        super().__init__(self.__species, name, age)
        self._angry = angry

    def __str__(self):
        return f"{super().__str__()}, она{' не ' if not self._angry else ' '}злая"


class Fish(Animal):
    class TypeFish(Enum):
        SEA_FISH = "морская"
        FRESHWATER_FISH = "пресноводная"

    __species = "рыба"
    def __init__(self, name: str, age: str, fish_type: TypeFish):
        super().__init__(self.__species, name, age)
        self._type = fish_type

    def __str__(self):
        return f"{super().__str__()}, она {self._type.value}"


if __name__ == '__main__':
    animals = [Cat("Барсик", 5, "рыжий"),
               Dog("Пират", 3, False),
               Fish("карась", 1, Fish.TypeFish.FRESHWATER_FISH),
               Fish("скат", 1, Fish.TypeFish.SEA_FISH),
               Dog("Барбос", 10, True)]
    for animal in animals:
        print(animal)
