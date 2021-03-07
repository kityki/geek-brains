"""
2. Сумма цифр числа
Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".

"""

print('Hello, user!')
number = input('Please, enter the number separated by coma\n>>> ')

my_list = list(map(int, number.split(' ')))
digit_sum = 0

for i in my_list:
    digit_sum = digit_sum + i
    print(digit_sum)

# Я хотела преобразовать число в список, чтобы было проще сложить цифры. Но что-то не получается здесь
# использовать while адекватно. Получается бесконечность. Арифметически решать не очень умею пока, поэтому решила так.
#  map я подсмотрела. Можно ли этот код довести до ума?

"""
решение преподавателя:

 number = input('Please, enter the number separated by coma\n>>> ')

 while number != '0':
    num = int(number)
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10

 print(digit_sum)
"""




















