"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
"""


user_dist = int(input('Введите ваш ежедневный результат:\n'))
target_dist = int(input('Введите желаемый результат:\n'))
result_dist = user_dist + user_dist * 0.1
day = 0
while result_dist <= target_dist:
    day += 1
    break
print(f'На {day} день результат будет {result_dist}.')




"""
Цикл не повторяется. Выдает только: На 1 день результат будет 2.2. 
Если break убрать, то получается беспонечноть. 
Очевидно, что накосячила в условии, но не пойму, что именно не так. 

"""
