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

