# кейс 4: вывод >> B process()
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

