'''
Функция get_the_fastest_func()

Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

    funcs — список произвольных функций
    arg — произвольный объект

Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила
на вычисление значения при вызове с аргументом arg наименьшее количество времени.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию
get_the_fastest_func(), но не код, вызывающий ее.
'''

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


def fun1(num):
    for i in range(num):
        time.sleep(0.5)
    return num


def fun2(num):
    for i in range(num):
        time.sleep(0.3)
    return num


def fun3(num):
    for i in range(num):
        time.sleep(0.4)
    return num


print(get_the_fastest_func([fun1, fun2, fun3], 3))
