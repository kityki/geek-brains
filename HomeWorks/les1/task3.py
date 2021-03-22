"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.

"""
print('Greetings, user!')

number = input('Enter a number.\n>>>')

numb1 = int(number)
numb2 = int(number*2)
numb3 = int(number*3)

res = numb1 + numb2 + numb3

print(f'{number} + {number*2} + {number*3} = {res}.')
