"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_phrase = input('Введите предложение: \n>>>')
string = user_phrase.split()

for el in range(len(string)):
    if len(string[el]) > 10:
        print(el + 1, string[el][:10])
        continue
    print(el + 1, string[el])

"""

user_input = input("Введите строку из нескольких слов через пробел")
string = user_input.split()

for i in range(len(string)):
    if len(string[i]) > 10:
        print(i + 1, ")", string[i][:10])
        continue
    print(i + 1, ")", string[i])

"""