'''Перепишите функцию product_of_odds() в функциональном стиле
с использованием встроенных функций filter() и reduce().

def product_of_odds(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result

Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование
встроенных функций filter() и reduce(), однако лучше сделать это задание честно 😃.
Примечание 2. Вызывать функцию product_of_odds() не нужно,
требуется только реализовать ее в функциональном стиле.'''


from functools import reduce
import operator


def product_of_odds(data):
    f_data = filter(lambda num: num % 2 == 1, data)
    return reduce(operator.mul, f_data, 1)


data = list(range(1, 10))

print(product_of_odds(data))
