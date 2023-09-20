'''
Декоратор trace

Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения,
а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:

TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор trace,
но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello, World')

Sample Output 1:

TRACE: вызов say() с аргументами: ('Jane', 'Hello, World'), {}
TRACE: возвращаемое значение say(): 'Jane: Hello, World'

Sample Input 2:

@trace
def sub(a, b, c):
    'прекрасная функция'
    return a - b + c

print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)

Sample Output 2:

sub
прекрасная функция
TRACE: вызов sub() с аргументами: (20, 5), {'c': 10}
TRACE: возвращаемое значение sub(): 25

Из всех попыток 30% верных
Отличное решение!

'''


import functools

def trace(fun):
    @functools.wraps(fun)
    def inner(*args, **kwargs):
        result = fun(*args, **kwargs)
        print(f'TRACE: вызов {fun.__name__}() с аргументами: {args}, {kwargs}')
        if isinstance(result, str):
            print(f"TRACE: возвращаемое значение {fun.__name__}(): '{result}'")
        else:
            print(f'TRACE: возвращаемое значение {fun.__name__}(): {result}')
        return result
    return inner


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')

print('2')

@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c

print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)

print('3')

@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)

print('4')

@trace
def add(a, b, c):
    '''docs'''
    return a + b + c

print(add(1, 2, 3))
print(add.__name__)
print(add.__doc__)

print('5')

@trace
def add(a, b, c):
    '''docs'''
    return a + b + c

print(add(b=3, c=3, a=3))
print(add.__name__)
print(add.__doc__)

print('6')

@trace
def concat(a, b):
    '''concat two strings'''
    return a + b

print(concat('bee', b='geek'))
print(concat.__name__)
print(concat.__doc__)

print('7')

@trace
def func(nums):
    '''прекрасная функция'''
    return list(i ** 2 for i in nums)

print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6])

print('8')

@trace
def func(nums, degree=3):
    '''прекрасная функция'''
    return list(i**degree for i in nums)

print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6], degree = 5)

'''Накосячил
При решении надо было воспользоваться этим:
Встроенная функция repr() возвращает объект в формальном (понятном 
интерпретатору) строковом представлении.
чтобы не городить это:
    if isinstance(result, str):
        print(f"TRACE: возвращаемое значение {fun.__name__}(): '{result}'")'''