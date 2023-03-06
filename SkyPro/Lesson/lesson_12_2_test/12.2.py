# функция для теста
def add(x, y):
    return x + y

# тест через if
if add(-2, 2) != 0:
    raise Exception('Ошибка!')

# тест через assert
assert add(-2, 2) == 0

def abs(x):
    return -x

if __name__ == '__main__':
    assert abs(-2) == 2
    assert abs(-0) == 0
    #assert abs(2) == 2
    print('ok')