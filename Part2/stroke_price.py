'''для подсчета стоимости строки, исходя из того,
что один любой символ(в том числе пробел стоит 6060 копеек.'''

def price(stroke, char_price):

    a = len(stroke) * char_price
    b = int(a // 100)
    c = int(a % 100)

    price = str(b) + ' р. ' + str(c) + ' коп.'

    return price

char_price = 60

print(price(input(), char_price))