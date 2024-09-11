'''
Функция tabulate()

Реализуйте функцию tabulate(), которая принимает один аргумент:

    func — произвольная функция

Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых
значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию tabulate(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))

Sample Output 1:

1
2

Sample Input 2:

func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))

Sample Output 2:

11
12
13

Верно решили 948 учащихся
Из всех попыток 71% верных
Хорошие новости, верно! '''

from itertools import count


def tabulate(func):
    count1 = count(1)
    while True:
        yield func(next(count1))



func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))

print('test 2')

func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))

print('test 3')

func = lambda x: x ** 2
values = tabulate(func)

for _ in range(100):
    print(next(values))

print('test 4')

def func(n):
    return 'beegeek' * n

values = tabulate(func)

for _ in range(10):
    print(next(values))
