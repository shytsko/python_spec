# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

import Animals


class AnimalFactory:
    def __init__(self, animal_type: type, *args, **kwargs):
        self._animal_type = animal_type
        self._args = args
        self._kwargs = kwargs
        self._animal = None

    def get_animal(self):
        if not self._animal:
            self._animal = self._animal_type(*self._args, **self._kwargs)
        return self._animal


if __name__ == '__main__':
    cat_factory = AnimalFactory(Animals.Cat, "Барсик", 3, "белый")
    cat1 = cat_factory.get_animal()
    print(cat1)

    dog_factory = AnimalFactory(Animals.Dog, "Барбос", 3, True)
    dog1 = dog_factory.get_animal()
    print(dog1)

    fish_factory = AnimalFactory(Animals.Fish, "карась", 1, Animals.Fish.TypeFish.FRESHWATER_FISH)
    fish1 = fish_factory.get_animal()
    print(fish1)
