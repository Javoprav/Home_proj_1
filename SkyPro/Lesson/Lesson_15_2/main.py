class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        self.x += 1
        del self.y
        self.y = 0

class PointSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        self.x += 1
        del self.y
        self.y = 0

pt = Point(10, 20)
pt_slots = PointSlots(10, 20)

import sys
print(sys.getsizeof(pt))
print(sys.getsizeof(pt_slots))

import timeit
t1 = timeit.timeit(pt.get)  # без слотс
t2 = timeit.timeit(pt.get)  # с слотс

print(t1, t2)
print((t1-t2)/t1*100)
# print(pt.x)
pt.y = 50
pt.z = 100
print(pt.__dict__)
# pt_slots = Child(10, 20)
# pt_slots.z = 15