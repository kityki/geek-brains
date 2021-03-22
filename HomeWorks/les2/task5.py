"""
Задание 5

Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.
Например:
57 руб 08 коп, 46 руб 51 коп, 97 руб 00 коп, ...

Подумать, как из цены получить рубли и копейки, как добавить нули, если,
например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""


price_list = [7, 67.05, 456, 22, 56.15, 124.40, 14.20, 96, 3.09, 65, 39.07, 1]
print(id(price_list))

price_list.sort()

for i in price_list:
    ruble = int(i)
    kop = int(i * 100) % 100

    result = (f'{ruble} рублей и {kop:02} копеек')
    print(result)

print(id(price_list))

print('_____________')


# часть 2

price_list_reversed = sorted(price_list, reverse = True)

for i in price_list_reversed:
    ruble = int(i)
    kop = int(i * 100) % 100

    result = (f'{ruble} рублей и {kop:02} копеек')

    print(result)

print(id(price_list))

print('_____________')


# часть 3

for i in sorted(price_list_reversed[0:5]):
    ruble = int(i)
    kop = int(i * 100) % 100

    result = (f'{ruble} рублей и {kop:02} копеек')

    print(result)

print(id(price_list))

print('_____________')




#print(id(price_list))
#price_list.sort()
#print(price_list)
#print(id(price_list))





#for i in price_list:
#    if i > price_list[0] + 1:
#        a = i - i
#        print(i)

