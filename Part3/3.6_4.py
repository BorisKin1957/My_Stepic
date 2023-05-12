'''Вам доступны две реализации функции, которая создает и возвращает список из чисел
от 1 до 10000000 включительно:

    с использованием цикла for и метода append()
    с использованием списочного выражения

Определите, какая функция быстрее создаст и вернет требуемый список.'''

import time


def get_the_fastest_func(funcs, arg):
    tm_res = []
    for fun in funcs:
        start = time.perf_counter_ns()
        fun(arg)
        end = time.perf_counter_ns()
        tm_res.append(int(end - start))
    ind = tm_res.index(min(tm_res))

    return funcs[ind]


def for_and_append(iterations):  # с использованием цикла for и метода append()
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension(iterations):  # с использованием списочного выражения
    return [i + 1 for i in range(iterations)]


print(get_the_fastest_func([for_and_append, list_comprehension], 10 ** 7))

'''Как уже упоминалось в предыдущих курсах, списочные выражения являются 
предпочтительным способом создания списков, 
нежели использование цикла for и метода append().'''