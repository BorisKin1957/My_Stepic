'''
Декоратор add_attrs

Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов
и устанавливает их в качестве атрибутов декорируемой функции. Названием атрибута должно являться имя аргумента,
значением атрибута — значение аргумента.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Вспомните про атрибут функции __dict__.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
 а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор add_attrs,
но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'

print(beegeek.attr1)
print(beegeek.attr2)

Sample Output 1:

bee
geek

Sample Input 2:

@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'

print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)

Sample Output 2:

bee
geek
beegeek

Из всех попыток 69% верных
Верно. Так держать! '''


import functools


def add_attrs(**name_args):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        for key, value in name_args.items():
            wrapper.__dict__.setdefault(key, value)
        return wrapper
    return decor



@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'

print(beegeek.attr1)
print(beegeek.attr2)

print('2')


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)

print('3')


@add_attrs(attr1='bee', attr2='geek', attr3='stepik')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.attr3)
print(beegeek.__name__)
print(beegeek.__doc__)

print('4')


@add_attrs(at1=10, at2=20, at3=30, at4=40, atf=50)
def add(a, b):
    '''add docs'''
    return a + b


print(add.at1)
print(add.at2)
print(add.at3)
print(add.__name__)
print(add.__doc__)
print(add(1, 2))
print(add(b=12, a=13))
print(add.at4)
print(add.atf)

print('5')


@add_attrs(func_attr='i am attribute')
def func(a, b):
    '''func docs'''
    return


print(func.func_attr)