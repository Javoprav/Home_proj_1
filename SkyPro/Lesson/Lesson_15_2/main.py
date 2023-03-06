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

