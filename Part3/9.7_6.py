'''
Декоратор takes_positive

Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:

    TypeError, если аргумент не является целым числом
    ValueError, если аргумент является целым числом, но отрицательным или равным нулю

Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или
при наличии разных аргументов, несоответствующих разным условиям: TypeError, затем ValueError.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes_positive,
но не код, вызывающий его.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@takes_positive
def positive_sum(*args):
    return sum(args)

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

Sample Output 1:

55

Sample Input 2:

@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

Sample Output 2:

<class 'ValueError'>

Sample Input 3:

@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

Sample Output 3:

<class 'TypeError'>

Из всех попыток 37% верных
Абсолютно точно. '''


def takes_positive(fun):
    def inner(*args, **kwargs):
        if kwargs:
            args = list(args) + list(kwargs.values())
        for i in args:
            if isinstance(i, float):
                return TypeError
            elif i <= 0:
                return ValueError
        '''В ретурне важно убрать из аргументов функции kwargs, 
        поскольку мы ранее его преобразовали в args'''
        return fun(*args)
    return inner


@takes_positive
def positive_sum(*args):
    return sum(args)
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print()

@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

print()


@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

print()


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))


print()


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))