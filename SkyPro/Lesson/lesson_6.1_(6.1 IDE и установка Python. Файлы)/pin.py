def check_pin(pin):      # проверка пин кода
    if not pin.isdigit():
      return False
    if len(pin) != 4:
      return False
    return True

#  или так

'''def check_pin(pin):
    if len(pin) == 4 and pin.isdigit():    
        return True
    return False'''

        
try:
    assert check_pin("1234") == True
    assert check_pin("123") == False
    assert check_pin("a000") == False
    assert check_pin("0000") == True
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")