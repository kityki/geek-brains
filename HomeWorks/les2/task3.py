"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.

dict_seasons = {
    'Зима': (12, 1, 2),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}
"""


month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
season_list = ['зима', 'весна', 'лето', 'осень']


month = int(input('Введите номер месяца: \n>>>'))

if month in month_list[0:3]:
    print('Это зима.\n')

elif month in month_list[3:6]:
    print('Это весна.\n')

elif month in month_list[6:9]:
    print('Это лето.\n')

elif month in month_list[9:]:
    print('Это осень.\n')

elif month > 12:
    print('Введите число от 1 до 12.')


"""
month_list = ['hello', 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(month_list[10:])
"""
"""
numbers = [2, 10, 306, 568]
for num in numbers:
    result = num // 2
    print(f'Если {num} поделить на 2, то результат равен: {result}')
       
"""
