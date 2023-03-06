import datetime

class Employee:
    """Класс для представления сотрудника"""
    amn_rate = 1.04

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self) -> str:
        """Возврат ФИО"""
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, value: str) -> None:
        """Возврат email"""
        first, last = value.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self) -> None:
        """Устанавливает имя и фамилию в None"""
        print("Удаление")
        self.first = None
        self.last = None

    @property
    def email(self) -> str:
        """Возврат email"""
        return f'{self.first}.{self.last}@company.com'

    def raise_pay(self):
        self.pay *= self.amn_rate

    @classmethod
    def set_amn_raise(cls, new_value: float) -> None:
        """Обновляет уровень индексации зп"""
        cls.amn_rate = new_value

    @classmethod
    def init_from_str(cls, init_str: str) -> 'Employee':
        """Создает сотрудника из строки"""
        first, last, pay = init_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day: datetime) -> bool:
        """Возвращает True если день рабочий, иначе False"""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp = Employee('Kristina', 'Ronaldovna', 666)
print(emp.fullname)
print(emp.email)
emp.first = 'Kristianna'
print(emp.fullname)
print(emp.email)
emp.fullname = 'гари проппер'
print(emp.fullname)
print(emp.first)
del emp.fullname
print(emp.first)

emp1 = Employee('na', 'ovna', 1000)
emp2 = Employee('nana', 'Oovna', 2000)
print(emp1.pay)
Employee.set_amn_raise(1.3)
emp1.raise_pay()
print(emp1.pay)
emp2.raise_pay()
print(emp2.pay)

new_emp = Employee.init_from_str('Коля-Николай-1000')
print(new_emp.fullname)
print(new_emp.pay)
print(new_emp.is_workday(datetime.date(2023, 2, 19)))