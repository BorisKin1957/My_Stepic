'''
Декоратор retry

Реализуйте декоратор retry, который принимает один аргумент:

    times — натуральное число

Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка.
Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times,
после чего должен возбуждать исключение MaxRetriesException.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор retry, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@retry(3)
def no_way():
    raise ValueError

try:
    no_way()
except Exception as e:
    print(type(e))

Sample Output 1:

<class '__main__.MaxRetriesException'>

Sample Input 2:

@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')

beegeek()

Sample Output 2:

beegeek

Из всех попыток 51% верных
Верно. '''


import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while wrapper.count > 0 and wrapper.flag == True:
                try:
                    result = func(*args, **kwargs)
                    if result:
                        return result
                    wrapper.flag = False
                except:
                    wrapper.count -= 1
                    wrapper(*args, **kwargs)
            else:
                if wrapper.flag:
                    raise MaxRetriesException

        wrapper.count = times
        wrapper.flag = True

        return wrapper

    return decor


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))

print('2')


@retry(6)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 3:
        raise ValueError
    print('beegeek')

beegeek()

print('3')


@retry(6)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

print('4')


@retry(2)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 2:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

print('5')


@retry(5)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

print('6')


@retry(5)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))

print('8')


@retry(10)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 3:
        raise ValueError
    return a + b


try:
    print(add(10, 30))
except Exception as e:
    print(type(e))

print('9')


@retry(100)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b


try:
    print(add(40, 10))
except Exception as e:
    print(type(e))

print('11')


@retry(10)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c


try:
    print(calculate(1, 2, c=3))
except Exception as e:
     print(type(e))