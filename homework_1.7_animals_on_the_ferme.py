# homework_1.7_animals_on_the_ferme.py
# Задан базовых класс Ferme_animals, его наследуют на подкласса Big_animals и Feathery_animals.
# Парнокопытные животные наслеют класс Big_animals, пернатые наследуют класс Feathery_animals.


class FermeAnimals():
    '''Класс FermeAnimals

    Класс Ferme_animals является базовым для всех животных на ферме.
    В классе производится посчет поголовья животных на ферме и выводится
    информация по каждому животному.
    '''

    location = 'Ферма'
    animal_count = 0

    def __init__(self, name, type_animal, product, sounds):
        self.name = name
        self.type_animal = type_animal
        self.product = product
        self.sounds = sounds
        print('На ферме появилось новое животное: Тип {0} | Кличка {1} | Производит {2}'\
              .format(self.type_animal, self.name, self.product))
        FermeAnimals.animal_count += 1

    @staticmethod
    def how_many():
        print('Общее кол-во животных на ферме: {0}'.format(FermeAnimals.animal_count))

    def tell(self):
        print('Так как {0} - {1}, то издает такой звук: {2}"'.format(self.name, self.type_animal, self.sounds))


class BigAnimals(FermeAnimals): # класс крупных животных фермы
    '''Класс BigAnimals

    В него входят все животные фермы являющиеся парнокопытными,
    находящиеся в корпусе РКС.
    '''

    building_type = 'Корпус КРС'

    def __init__(self, name, type_animal, product, sounds):
        FermeAnimals.__init__(self, name, type_animal, product, sounds)

    def tell(self):
        FermeAnimals.tell(self)


class Cow(BigAnimals):
    # Подкласс Cow(корова) класса BigAnimals

    type_animal = 'Корова'
    product = 'Молоко'
    sounds = 'Му-у-у-у-у'

    def __init__(self, name):
        self.type_animal = Cow.type_animal
        self.product = Cow.product
        self.sounds = Cow.sounds
        BigAnimals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        BigAnimals.tell(self)


class Goat(BigAnimals):
    # Подкласс Goat(коза) класса BigAnimals

    type_animal = 'Коза'
    product = ['молоко', 'шесть']
    sounds = 'Ме-е-е-е'

    def __init__(self, name):
        self.type_animal = Goat.type_animal
        self.product = Goat.product
        self.sounds = Goat.sounds
        BigAnimals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        BigAnimals.tell(self)


class Sheep(BigAnimals):
    # Подкласс Sheep(овца) класса BigAnimals

    type_animal = 'Овца'
    product = ['молоко', 'шесть']
    sounds = 'Беееее'

    def __init__(self, name):
        self.type_animal = Sheep.type_animal
        self.product = Sheep.product
        self.sounds = Sheep.sounds
        BigAnimals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        BigAnimals.tell(self)


class Pig(BigAnimals):
    # Подкласс Pig(свинья) класса BigAnimals

    type_animal = 'Свинья'
    product = 'мясо'
    sounds = 'Хрю-хрю-хрю'

    def __init__(self, name):
        self.type_animal = Pig.type_animal
        self.product = Pig.product
        self.sounds = Pig.sounds
        BigAnimals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        BigAnimals.tell(self)


class FeatheryAnimals(FermeAnimals):
    '''Класс FeatheryAnimals

    В него входят все пернатые животные фермы,
    находящиеся в корпусе пернатых.
    '''

    building_type = 'Корпус пернатых'

    def __init__(self, name, type_animal, product, sounds):
        FermeAnimals.__init__(self, name, type_animal, product, sounds)

    def tell(self):
        FermeAnimals.tell(self)


class Duck(FeatheryAnimals):
    # Подкласс Duck(утка) класса FeatheryAnimals

    type_animal = 'Утка'
    product = 'утиное мясо'
    sounds = 'Кря-кря-кря'

    def __init__(self, name):
        self.type_animal = Duck.type_animal
        self.product = Duck.product
        self.sounds = Duck.sounds
        FeatheryAnimals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        FeatheryAnimals.tell(self)


class Chicken(FeatheryAnimals):
    # Подкласс Chicken(курица) класса FeatheryAnimals

    type_animal = 'Курица'
    product = ['яйца', 'куриное мясо ']
    sounds = 'Ко-ко-ко'

    def __init__(self, name):
        self.type_animal = Chicken.type_animal
        self.product = Chicken.product
        self.sounds = Chicken.sounds
        FeatheryAnimals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        FeatheryAnimals.tell(self)

class Geese(FeatheryAnimals):
    # Подкласс Geese(гусь) класса FeatheryAnimals

    type_animal = 'Гусь'
    product = 'гусиное мясо'
    sounds = 'Га-га-га'

    def __init__(self, name):
        self.type_animal = Geese.type_animal
        self.product = Geese.product
        self.sounds = Geese.sounds
        FeatheryAnimals.__init__(self, name, self.type_animal, self.product, self.sounds)

    def tell(self):
        FeatheryAnimals.tell(self)


# Создадим экземпляры класса

cow = Cow('Буренка')
goat = Goat('Колокольчик')
sheep = Sheep('Снежка')
pig_1 = Pig('Борька')
pig_2 = Pig('Васька')
duck = Duck('Серая Шейка')
chicken = Chicken('Кудахталка')
goose = Geese('Декстер')
print('') # вывели пустую строку

all_animals = [cow, goat, sheep, pig_1, pig_2, duck, chicken, goose]
print('Какие звуки издают животные на ферме:')
for animal in all_animals:
    animal.tell()

# Подсчет кол-во животных на ферме
FermeAnimals.how_many()
