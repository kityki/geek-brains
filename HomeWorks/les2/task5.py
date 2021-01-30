"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""


rating_list = [9, 6, 4, 4, 2]

i = 0
user_number = (input('Введите натуральное число:\n>>> '))

while True:
    if user_number.isdigit():
        user_number = int(user_number)
        break
    print('Вы ввели не чило. Введите натурально число.')

while True:
    if user_number in rating_list:
        pos_num = rating_list.index(user_number)
        rating_list.insert(pos_num, user_number)
        break
    elif user_number > rating_list[i]:
        rating.insert(i, user_number)
        break
    elif i < len(rating_list) - 1:
        i += 1
        continue
    else:
        rating_list.append(user_number)
        break

print(rating_list)



