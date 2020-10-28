"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""

user_number = int(input('Введите целое положительное число\n'))
result = 0
while user_number and result != 9:
    tmp = user_number % 10
    if tmp > result:
        result = tmp
        user_number //= 10
        print(result)


