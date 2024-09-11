'''
Декоратор ignore_exception

Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных аргументов — 
типов исключений, и выводит текст:

Исключение <тип исключения> обработано

если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.

Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор ignore_exception, 
но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x
    
f(0)

Sample Output 1:

Исключение ZeroDivisionError обработано

Sample Input 2:

min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))

Sample Output 2:

<class 'TypeError'>

Из всех попыток 48% верных
Правильно, молодец! '''

import functools


def ignore_exception(*all_exep):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                if err.__class__ in all_exep:
                    print(f'Исключение {type(err).__name__} обработано')
                else:
                    raise err.__class__

        return wrapper

    return decor


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x

f(0)

print('2')

min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))

print('4')


@ignore_exception(TypeError)
def func():
    '''func docs'''
    raise ValueError


try:
    func()
except Exception as e:
    print(type(e))

print('6')


@ignore_exception(ValueError, TypeError, NameError)
def func():
    '''func docs'''
    raise NameError


try:
    func()
except Exception as e:
    print(type(e))

print('9')


@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    return 'beegeek'


print(beegeek())


