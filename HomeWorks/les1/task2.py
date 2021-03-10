"""
2. Сумма цифр числа
Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".

"""

print('Hello, user!')
number = input('Please, enter the number separated by coma\n>>> ')

my_list = list(map(int, number.split(' ')))
digit_sum = 0

for i in (my_list):
    if number == '0':
        print('You have entered 0')
    else:
        digit_sum += i
        print(digit_sum)



# Добрый день! Как доработать это решение так, чтобы, например, вводя цифры 6 7,
# он не выдавал в столбик сначала 6, потом 13. Как здесь можно вывести сразу 13?
# Или с for так не получится, а только с while?

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




















