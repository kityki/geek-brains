"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

print('Hello, user!')

profit = int(input('Please, enter the number of the profit:\n>>>'))
expenses = int(input('Please, enter the number of the expenses:\n>>>'))

if profit > expenses:

    print('The company is profitable.')

    revenue = int(input('Please, enter the number of the revenue:\n>>>'))
    profit_margin = round(profit / revenue * 100)
    print(f'The Profit Margin is {profit_margin}%.')

    employee = int(input('Please, enter the number of employees:\n>>>'))
    profit_per_person = profit_margin / employee
    print(f'The Profit per Person is {profit_per_person}.')


else:
    loses = int(expenses - profit)
    print(f'The company has a negative balance sheet. Loses are {loses} USD.')



