'''Вам доступны три реализации функции, которая принимает в качестве аргумента
итерируемый объект и возвращает список, элементами которого являются элементы переданного итерируемого объекта:

    с использованием цикла for и метода append()
    с использованием списочного выражения
    с использованием встроенной функции list()

Определите, какая функция быстрее создаст и вернет список на основе итерируемого объекта range(100_000)'''

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


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100000)))

'''В случае если требуется создать список на основе итерируемого объекта или коллекции 
без какого-либо изменения элементов, то лучшим вариантом будет функция list().'''