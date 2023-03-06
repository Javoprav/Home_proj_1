from accessify import private, protected


class Employee:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    # в классе Employee
    @private
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp = Employee('Jon', 'Snow')
# обращаемся к атрибутам экземпляра класса
# print(emp.__first, emp.__last)

print(dir(emp))
print(emp._Employee__first, emp._Employee__last)
Employee.set_raise_amt(1.05)