'''Вам доступны три реализации функции, которая вычисляет факториал числа n:

    встроенная из модуля math
    рекурсивная
    итеративная

Выясните, какая функция быстрее вычислит факториал числа 900.'''

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


from math import factorial  # функция из модуля math


def factorial_recurrent(n):  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):  # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(get_the_fastest_func([factorial, factorial_recurrent, factorial_classic], 900))