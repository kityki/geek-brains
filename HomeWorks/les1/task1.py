"""
ЗАДАНИЕ 1

Человеко-ориентированное представление интервала времени
Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:

1) до минуты: <s> сек;
2) до часа: <m> мин <s> сек;
3) до суток: <h> час <m> мин <s> сек;
4) сутки или больше: <d> дн <h> час <m> мин <s> сек

Например, если пользователь введет 4567 секунд, вывести:
1 час 16 мин 7 сек
"""

print('Hello, user!')

number = int(input('Enter the number of seconds to convert it in DD:HH:MM:SS format.\n>>> '))

hours = int(number / 60**2)
hours_sec = hours * 60**2

minutes = int((number - hours_sec) / 60)
minutes_sec = minutes * 60

day = int((number / (24*60*2)))
day_sec = day * (24*60*2)

seconds = number - (hours_sec + minutes_sec)

time = f'The result is: HH {hours}, MM {minutes}, SS {seconds}.'
print(time)

"""
Добрый день! Код рабоатет хорошо с минутами и часами, но когда я добавляю дни почему-то выходит так:

...
day = int((number / (24*60*2)))
day_sec = day * (24*60*2)
seconds = number - (day_sec + hours_sec + minutes_sec)

>>> 8700
The result is: DD 8640, HH 2, MM 25, SS -8640.

Почему без дней он все хорошо считает, а с ними выходит что-то непонятное?
Ваше решение посмотрела. Но мне интересно, как можно доработать мое. Заранее спасибо! 
"""

