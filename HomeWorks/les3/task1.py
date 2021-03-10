"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def devide(a, b):
    a, b = int(a), int(b)
    if b != 0:
        c = a // b
        return(c)


devide(100, 2)

"""

def div(a, b):
    try:
        a, b = int(a), int(b)
        result = a / b
    except ValueError:
        return "Value Erroe"
    except ZeroDivisionError:
        return "Division by zero is impossible."
    return round(result)


print(div(10, 5))
"""