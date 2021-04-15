"""
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере,
посмотреть содержимое ответа.
"""

import requests

def get_currency_rate(currency):

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code != 200:
        print('В данный момент сайт не доступен.')
        exit()

    content = (response.content.decode('windows-1251'))
    parts = content.split('</Valute><Valute')
    currency = currency.upper()
    currency_code = '<CharCode>' + currency + '</CharCode>'
    for part in parts:
        if currency_code in part:
            break
    else:
        return None

    currency_rate = float(part.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))

    return currency_rate



print("USD", get_currency_rate('usd'))
print('EUR', get_currency_rate('EUR'))
