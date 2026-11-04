from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self._age}'

    def __len__(self):
        return len(self.name)
    
    @staticmethod
    def is_adult(age):
        return age >= 1

    @abstractmethod
    def make_sound(self):
        pass

    def get_age(self):
        return self._age

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} гав')

class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} мяу')

dog1 = Dog('Бобик', 5)
cat1 = Cat('Мурзик', 3)

dog1.make_sound()
cat1.make_sound()

print(f'Возраст {dog1.get_age()}')
print(f'Возраст {cat1.get_age()}')
print(dog1)
print(cat1)
print(f'Длина имени: {len(dog1)}')
print(f'Длина имени: {len(cat1)}')
print(f'Бобик взрослый? {Animal.is_adult(dog1.get_age())}')
print(f'Мурзик взрослый? {Animal.is_adult(cat1.get_age())}')
