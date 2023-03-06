from abc import ABC, abstractmethod

"""Абстрактный класс"""


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print('На машине')

    def stop(self):
        print('Машина остановлена')


class Moto(Vehicle):
    def go(self):
        print('На мото')

    def stop(self):
        print('Мото остановлен')


# veh = Vehicle()
car = Car()
moto = Moto()
# veh.go()
car.go()
moto.go()
car.stop()
moto.stop()

"""Множественное наследование и MRO"""


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # super().__init__()


class Mixinlog:
    ID = 0

    def __init__(self, *args):
        cls = type(self)
        cls.ID += 1
        self.id = cls.ID
        """Mixinlog.ID += 1           # альтер не раб
        self.id = Mixinlog.ID"""
        super().__init__(*args)

    def get_order(self):
        print(f'{self.id}-й сотрудник.')


class Dev(Mixinlog, Employee):
    pass


print(Dev.__mro__)  # цепочка наследования
dev1 = Dev('Dima', 'Medved')
dev2 = Dev('Vovk', 'Putini')
dev1.get_order()
dev2.get_order()
print(dev1.name)
print(dev1.surname)


# super() для множественного наследования
#  D > B > C > A
class A:
    def __init__(self):
        print('A.__init__()')


class B(A):
    def __init__(self):
        print('B.__init__()')


class C(A):
    def __init__(self):
        print('C.__init__()')


class D(B, C):
    def __init__(self):
        super(B, self).__init__()  # super(B, self).__init__() >>  C.__init__()
                            # super(C, self).__init__() >>  A.__init__()

print(D.mro())
obj = D()


# кейс 1: вывод >> A process()
class A:
    def process(self):
        print('A process()')
class B:
    pass
class C(A, B):
    pass
obj = C()
obj.process()  # кейс 1: вывод >> A process()


# кейс 2: вывод >> A process()
class A:
    def process(self):
        print('A process()')
class B:
    def process(self):      #  с новым методом
        print('B process()')
class C(A, B):
    pass
obj = C()
obj.process()  # кейс 2: вывод >> A process()

# кейс 3: вывод >> B process()
class A:
    pass
class B:
    def process(self):
        print('B process()')
class C(A, B):
    pass
obj = C()
obj.process()

# кейс 4: вывод >> C process()
class A:
    pass
class B:
    def process(self):
        print('B process()')
class C(A, B):
    def process(self):
        print('C process()')
obj = C()
obj.process()

# кейс 5: вывод >> B process()
class A:
    def process(self):
        print('A process()')
class B:
    def process(self):
        print('B process()')
class C(A, B):
    def process(self):
        print('C process()')
class D(C, B):    # class D(B, C): >> ошибка mro
    pass

obj = D()
# obj = C()
obj.process()

