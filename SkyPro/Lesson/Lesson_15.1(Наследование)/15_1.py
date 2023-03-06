class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        else:
            raise ValueError('Только объекты Employee')


# dev1 = Developer('Leo', 'Messi', 60_000)
# foo = 10

# dev1.apply_raise = foo
# print(dev1.apply_raise)
# print(dev1.pay)

dev2 = Developer('Leo', 'Messi', 60_000, 'Python')
dev3 = Developer('Leo', 'Messi', 60_000, 'Java')

print(dev2 + dev3)
print(dev2 + 10)