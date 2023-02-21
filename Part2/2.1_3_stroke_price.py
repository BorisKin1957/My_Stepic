'''подсчет стоимости строки, исходя из того,
что один любой символ(в том числе пробел) стоит 60 копеек.'''

def price(stroke, char_price):

    a = len(stroke) * char_price
    b = a // 100
    c = a % 100

    price = [b, 'р.', c, 'коп.']

    return price

char_price = 60

print(*price(input(), char_price))