'''
Декоратор reverse_args

Реализуйте декоратор reverse_args, который передает все позиционные аргументы
в декорируемую функцию func в обратном порядке.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор reverse_args,
но не код, вызывающий его.﻿

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@reverse_args
def power(a, n):
    return a ** n

print(power(2, 3))

Sample Output 1:

9

Sample Input 2:

@reverse_args
def concat(a, b, c):
    return a + b + c

print(concat('apple', 'cherry', 'melon'))

Sample Output 2:

meloncherryapple

Верно. '''

def reverse_args(fun):
    def inner(*args, **kwargs):
        args = args[::-1]
        return fun(*args, **kwargs)

    return inner


@reverse_args
def concat(a, b, c):
    return a + b + c
print(concat('apple', 'cherry', 'melon'))

print()


@reverse_args
def power(a, n):
    return a ** n
print(power(2, 3))

print()

@reverse_args
def operation(a, b, c):
    return a // b + c
print(operation(10, 20, 80))

print()

@reverse_args
def operation(a, b):
    return a // b

try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

print()

@reverse_args
def operation(a, b, name):
    return a // b + name
print(operation(10, 90, name=1))