import datetime


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # в классе Employee
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# создаем дату и вызываем метод
my_date = datetime.date(2023, 1, 31)
print(Employee.is_workday(my_date))


# создаем строку и вызываем метод
emp_str_1 = 'Jon-Snow-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())

