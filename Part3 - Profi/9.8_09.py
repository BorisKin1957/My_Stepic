'''
Декоратор takes

Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов,
каждый из которых является типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат одному из этих типов.
Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes,
но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))

Sample Output 1:

beebeebee

Sample Input 2:

@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))

Sample Output 2:

<class 'TypeError'>


Из всех попыток 39% верных
Прекрасный ответ. '''


import functools


def takes(*type_args):
    def decor(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            flag = True
            result = func(*args, **kwargs)
            L = [i for i in kwargs.values()]
            L.extend(args)
            for i in L:
                if type(i) not in type_args:
                    flag = False
                    break
            if flag:
                return result
            else:
                raise TypeError
        return inner
    return decor

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))

print('2')

@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))

print('4')

@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], 3))
except TypeError as e:
    print(type(e))

print('7')

@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add(1, b=2))
except TypeError as e:
    print(type(e))

print('11')


@takes(str)
def beegeek(word, repeat):
    return word * repeat


try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e))