"""
ЗАДАНИЕ 4

Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""


"""
# Решение 1

percent = int(input('Введите процент (число)\n>>> '))

a = [1]
b = list(range(2, 5))
c = list(range(5, 101))

# number = ''.join(percent)

if percent in a:
    print(f'{percent} процент')
elif percent in b:
    print(f'{percent} процента')
elif percent in c:
    print(f'{percent} процентов')


"""
# Решение 2.

percent = int(input('Введите процент (число)\n>>> '))

a = [1]
b = list(range(2, 5))
c = list(range(5, 101))

number = list(percent)
print(number)

""""

if percent[-1] == a:
    print(f'{(percent)} процент')

elif percent[-1] == b:

    print(f'{str(number)} процента')

elif percent[-1] == c:

    print(f'{str(number)} процентов')
"""



"""
a = list(range(2, 5))
b = list(range(5, 101))

if percent == 1:
    print(f'{percent} процент')
elif percent == len(a):
        print(f'{percent} процента')
else:
    percent == len(b)
    print(f'{percent} процентов')
"""












"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""
"""
user_number = int(input('Введите целое положительное число\n'))
result = 0
while user_number and result != 9:
    tmp = user_number % 10
    if tmp > result:
        result = tmp
        user_number //= 10
        print(result)
"""


