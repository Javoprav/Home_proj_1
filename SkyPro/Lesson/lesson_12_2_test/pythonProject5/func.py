def my_func(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error"