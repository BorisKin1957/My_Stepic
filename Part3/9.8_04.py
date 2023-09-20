'''
Декоратор prefix

Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:

    string — произвольная строка
    to_the_end — булево значение, по умолчанию равное False

Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции.
Если to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор prefix,
но не код, вызывающий его.

Примечание 4. Тестовые данные доступны по по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@prefix('€')
def get_bonus():
    return '2000'

print(get_bonus())

Sample Output 1:

€2000

Sample Input 2:

@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'

print(get_bonus())

Sample Output 2:

2000$$$

Из всех попыток 63% верных
Так точно!
'''


import functools


def prefix(string, to_the_end=False):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if to_the_end:
                return f'{result}{string}'
            else:
                return f'{string}{result}'
        return wrapper
    return decor



@prefix('€')
def get_bonus():
    return '2000'

print(get_bonus())

print('2')


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'

print(get_bonus())

print('3')


@prefix(' online-school', to_the_end=True)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())

print('4')


@prefix('online-school ')
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())

print('5')


@prefix('online-school ')
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()


print(make_lower.__name__)
print(make_lower.__doc__)
print(make_lower('beegeek', False))

print('6')


@prefix(' rocks', True)
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()


print(make_lower.__name__)
print(make_lower.__doc__)
print(make_lower('Beegeek'))