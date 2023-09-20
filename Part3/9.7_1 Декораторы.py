'''
Декоратор sandwich

Реализуйте декоратор sandwich, который выводит тексты:

---- Верхний ломтик хлеба ----

---- Нижний ломтик хлеба ----

до и после вызова декорируемой функции соответственно.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор sandwich,
но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

Sample Output 1:

---- Верхний ломтик хлеба ----
томат | салат | сыр | бекон
---- Нижний ломтик хлеба ----

Sample Input 2:

@sandwich
def beegeek():
    return 'beegeek'

print(beegeek())

Sample Output 2:

---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
beegeek

Хорошая работа. '''

def sandwich(fun):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        '''в следующей строке важно понять, что функция будет выполнена
         (те, ели в ней пинт, то выводит на печать) ее результат запомнен в переменной result'''
        result = fun(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result
    return wrapper


# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))
# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

# print()

# @sandwich
# def beegeek():
#     return 'beegeek'
# print(beegeek())
#
# print()
#
@sandwich
def counter():
    for i in range(3):
        print(i)
counter()
#
# print()
#
# @sandwich
# def counter(*args, **kwargs):
#     for i in args + tuple(kwargs.keys()) + tuple(kwargs.values()):
#         print(i)
#
# counter(10, 20, 30, sep='40', end='!!!', step='beegeek')

'''ПРАВИЛЬНОЕ, на мой взгляд, РЕШЕНИЕ

def sandwich(fun):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = fun(*args, **kwargs)
        if result:
            print(result)
            return '---- Нижний ломтик хлеба ----'
        else:
            print('---- Нижний ломтик хлеба ----')
            return result
    return wrapper


Потому что формирует результат:

---- Верхний ломтик хлеба ----
beegeek
---- Нижний ломтик хлеба ----'''