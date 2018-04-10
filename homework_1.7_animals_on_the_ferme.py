# homework_1.7_animals_on_the_ferme.py
# Задан базовых класс Ferme_animals, его наследуют на подкласса Big_animals и Feathery_animals.
# Парнокопытные животные наслеют класс Big_animals, пернатые наследуют класс Feathery_animals.

from requests import requests


class Ferme_animals():
    location = 'Ферма'
    animal_count = 0

    def __init__(self, name, type_animal, product, sounds):
        self.name = name
        self.type_animal = type_animal
        self.product = product
        self.sounds = sounds
        print('На ферме появилось новое животное: Тип {0} | Кличка {1} | Производит {2}'.format(self.type_animal, self.name, self.product))
        Ferme_animals.animal_count += 1

    @staticmethod
    def how_many():
        print('Общее кол-во животных на ферме: {0}'.format(Ferme_animals.animal_count))

    def tell(self):
        print('Так как {0} - {1}, то издает такой звук: {2}"'.format(self.name, self.type_animal, self.sounds))


class Big_animals(Ferme_animals): # класс крупных животных фермы
    building_type = 'Корпус КРС'

    def __init__(self, name, type_animal, product, sounds):
        Ferme_animals.__init__(self, name, type_animal, product, sounds)

    def tell(self):
        Ferme_animals.tell(self)


class Cow(Big_animals):
    type_animal = 'Корова'
    product = 'Молоко'
    sounds = 'Му-у-у-у-у'

    def __init__(self, name):
        self.type_animal = Cow.type_animal
        self.product = Cow.product
        self.sounds = Cow.sounds
        Big_animals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        Big_animals.tell(self)


class Goat(Big_animals): # класс коза
    type_animal = 'Коза'
    product = ['молоко', 'шесть']
    sounds = 'Ме-е-е-е'

    def __init__(self, name):
        self.type_animal = Goat.type_animal
        self.product = Goat.product
        self.sounds = Goat.sounds
        Big_animals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        Big_animals.tell(self)


class Sheep(Big_animals): # класс овца
    type_animal = 'Овца'
    product = ['молоко', 'шесть']
    sounds = 'Беееее'

    def __init__(self, name):
        self.type_animal = Sheep.type_animal
        self.product = Sheep.product
        self.sounds = Sheep.sounds
        Big_animals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        Big_animals.tell(self)


class Pig(Big_animals): # класс свинья
    type_animal = 'Свинья'
    product = 'мясо'
    sounds = 'Хрю-хрю-хрю'

    def __init__(self, name):
        self.type_animal = Pig.type_animal
        self.product = Pig.product
        self.sounds = Pig.sounds
        Big_animals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        Big_animals.tell(self)


class Feathery_animals(Ferme_animals): # класс пернатых животных
    building_type = 'Корпус пернатых'

    def __init__(self, name, type_animal, product, sounds):
        Ferme_animals.__init__(self, name, type_animal, product, sounds)

    def tell(self):
        Ferme_animals.tell(self)


class Duck(Feathery_animals): # класс утка
    type_animal = 'Утка'
    product = 'утиное мясо'
    sounds = 'Кря-кря-кря'

    def __init__(self, name):
        self.type_animal = Duck.type_animal
        self.product = Duck.product
        self.sounds = Duck.sounds
        Feathery_animals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        Feathery_animals.tell(self)


class Chicken(Feathery_animals): # класс курица
    type_animal = 'Курица'
    product = ['яйца', 'куриное мясо ']
    sounds = 'Ко-ко-ко'

    def __init__(self, name):
        self.type_animal = Chicken.type_animal
        self.product = Chicken.product
        self.sounds = Chicken.sounds
        Feathery_animals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        Feathery_animals.tell(self)

class Geese(Feathery_animals): # класс гусь
    type_animal = 'Гусь'
    product = 'гусиное мясо'
    sounds = 'Га-га-га'

    def __init__(self, name):
        self.type_animal = Geese.type_animal
        self.product = Geese.product
        self.sounds = Geese.sounds
        Feathery_animals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        Feathery_animals.tell(self)

# Создадим экземпляры класса
c = Cow('Буренка')
g = Goat('Колокольчик')
s = Sheep('Снежка')
p = Pig('Борька')
d = Duck('Серая Шейка')
ch = Chicken('Кудахталка')
ge = Geese('Декстер')
print('') # вывели пусткую строчку
all_animals = [c, g, s, p, d, ch, ge]
print('Какие звуки издают животные на ферме:')
for animal in all_animals:
    animal.tell()

# Подсчет кол-во животных на ферме
Ferme_animals.how_many()
