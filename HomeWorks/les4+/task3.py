"""
Задание 3. * Курс Валюты (расширенный)
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date.

"""
import datetime
import decimal
import requests

def get_currency_rate(currency):

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code != 200:
        print('В данный момент сайт не доступен.')
        exit()
    content = (response.content.decode('windows-1251'))

    day, month, year = list(map(int, content.split('Date="')[1].split('"', maxsplit=1)[0].split('.')))
    current_date = datetime.date(year, month, day)

    parts = content.split('</Valute><Valute')
    currency = currency.upper()
    currency_code = '<CharCode>' + currency + '</CharCode>'
    for part in parts:
        if currency_code in part:
            currency_rate = decimal.Decimal(part.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))

            break
    else:
        currency_rate = None


    return currency_rate, current_date


print(get_currency_rate('usd'))
print(get_currency_rate('EUR'))


# Почему возвращается так? Как убрать Desimal через print?
#(Decimal('76.0734'), datetime.date(2021, 4, 3))
#(Decimal('89.5916'), datetime.date(2021, 4, 3))
#