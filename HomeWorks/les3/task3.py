"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""




"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(num_1, num_2, num_3):
    num_1, num_2, num_3 = int(num_1), int(num_2), int(num_3)
    n = [num_1, num_2, num_3]
    for i in n:
        if i < num_1 and i < num_2:
            summ = num_1 + num_2
            return summ
        elif i < num_1 and i < num_3:
            summ = num_1 + num_3
            return summ
        elif i < num_2 and i < num_3:
            summ = num_2 + num_3
            return summ



print(my_func(8, 45, 543))