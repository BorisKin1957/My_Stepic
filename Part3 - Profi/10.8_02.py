'''
Функция factorials()

Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:

    n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является
факториалом очередного натурального числа.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию factorials(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = factorials(6)

print(*numbers)

Sample Output 1:

1 2 6 24 120 720

Sample Input 2:

numbers = factorials(2)

print(next(numbers))
print(next(numbers))

Sample Output 2:

1
2


Верно решили 969 учащихся
Из всех попыток 85% верных
Отличное решение! '''


from itertools import accumulate
import operator


def factorials(n):
    l = range(1, n + 1)
    yield from (accumulate(l, operator.mul))


numbers = factorials(6)

print(*numbers)

print('test 2')

numbers = factorials(2)

print(next(numbers))
print(next(numbers))

print('test 3')

numbers = factorials(100)

print(*numbers)


print('test 4')

numbers = factorials(1001)

for _ in range(1000):
    next(numbers)

print(next(numbers))