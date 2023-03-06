'''**Задача 1**

Напишите класс `Rectangle` с атрибутами длины и ширины.

Создайте метод `perimeter()` для вычисления периметра
 прямоугольника и метод `area()` для вычисления площади
  прямоугольника.

Создайте метод `display()`, который отображает длину,
 ширину, периметр и площадь экземпляра класса `Rectangle`.'''

class Rectangle:

    def __init__(self, dlin, shir):
        self.dlin = dlin
        self.shir = shir

    def perimeter(self):
        return self.dlin + self.shir * 2

    def area(self):
        return self.dlin * self.shir

    def display(self):
        return f'{self.dlin}{self.shir}{self.perimeter()}{self.area()}'


pr = Rectangle(33, 33)
print(pr.perimeter())
print(pr.area())
print(pr.display())

'''**Задача 2**

Создайте класс `Person`, содержащим два атрибута: имя и
 возраст.

Создайте метод-класса `fromBirthYear` с альтернативным
 способом создания экземпляра класса `Person` - когда
  указан год рождения.

```python
person = Person('Иван', 19)
person.display()

person1 = Person.fromBirthYear('Николай',  2000)
person1.display()

# вывод
Иван. Возраст: 19
Николай. Возраст: 23
```

<aside>
💡 Получить текущий год можно так:
`from datetime import date`
`print(date.today().year)`
</aside>'''

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, age_birt):
        birth = date.today().year - age_birt
        return Person(name, birth)

    def display(self):
        return f'{self.name} {self.age}'


person = Person('Иван', 19)
print(person.display())
person1 = Person.fromBirthYear('Николай',  2000)
print(person1.display())
print(date.today().year)
# Иван. Возраст: 19
# Николай. Возраст: 23
# <aside>
# 💡 Получить текущий год можно так:
# `from datetime import date`
# `print(date.today().year)`
# </aside>

'''**Задача 3**

В задаче 2 сделать атрибуты приватными. Написать к ним
 сеттеры, чтобы имя было строкой и содержало только буквы,
  а возраст был больше нуля и меньше 120.
'''

from datetime import date

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @classmethod
    def fromBirthYear(cls, name, age_birt):
        birth = date.today().year - age_birt
        return Person(name, birth)

    @property
    def display(self):
        return f'{self.__name} {self.__age}'

    @display.setter
    def display(self, name, age):
        if name.isalpha():
            self.__name = str(name)
        elif age > 0 and age < 120:
            self.__age = age


person = Person('Иван', 19)
print(person.display)
person1 = Person.fromBirthYear('Николай',  2000)
print(person1.display)
print(date.today().year)