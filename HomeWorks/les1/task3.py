"""
Сумма чисел из списка *
Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):

1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!

2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
сумма цифр которых делится нацело на 7.

3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков
"""

# у меня решение не получилось. Потом уже посмотрела Ваше решение.

cubes = []
number = 1
while number < 1000:
    cubes.append(number**3)
    number += 2

sum_of_numbers = 0
for number in cubes:
    sum_of_digits = 0
    n1 = number
    while n1 > 0:
        sum_of_digits += n1 % 10
        n1 //= 10
    if sum_of_digits % 7 == 0:
        sum_of_numbers += number
print(sum_of_numbers)

# part 2

new_cubes = []
for number in cubes:
    new_cubes.append(number + 17)

sum_of_numbers = 0
for number in new_cubes:
    sum_of_digits = 0
    n1 = number
    while n1 > 0:
        sum_of_digits += n1 % 10
        n1 //= 10
    if sum_of_digits % 7 == 0:
        sum_of_numbers += number
print(sum_of_numbers)

# part 3

sum_of_numbers = 0
num = 1
while num < 1000:
    number = num**3 + 17

    sum_of_digits = 0
    n1 = number
    while n1 > 0:
        sum_of_digits += n1 % 10
        n1 //= 10

    if sum_of_digits % 7 == 0:
        sum_of_numbers += number

    num += 2


"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.

print('Greetings, user!')

number = input('Enter a number.\n>>>')

numb1 = int(number)
numb2 = int(number*2)
numb3 = int(number*3)

res = numb1 + numb2 + numb3

print(f'{number} + {number*2} + {number*3} = {res}.')
"""