'''
Функция take()

Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность из первых
n элементов итерируемого объекта iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны
располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию take(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:



Sample Input 1:

print(*take(range(10), 5))

Sample Output 1:

0 1 2 3 4

Sample Input 2:

iterator = iter('beegeek')

print(*take(iterator, 22))

Sample Output 2:

b e e g e e k

Sample Input 3:

iterator = iter('beegeek')

print(*take(iterator, 1))

Sample Output 3:

b

Верно решили 980 учащихся
Из всех попыток 89% верных
Хорошая работа. '''

from itertools import islice

def take(iterable, n):
    return islice(iterable, n)

print(*take(range(10), 5))


print('test 2')

iterator = iter('beegeek')

print(*take(iterator, 22))

print('test 3')

iterator = iter('beegeek')

print(*take(iterator, 1))

print('test 4')

iterator = take(iter('beegeek'), 2)

print(next(iterator))
print(next(iterator))

print('test 5')

iterator = iter('stepik')

print(*take(iterator, 6))

print('test 6')

iterator = iter('stepik')

print(*take(iterator, 5))

print('test 7')

iterator = iter('s')

print(*take(iterator, 1))

print('test 8')

iterator = iter([0])

print(*take(iterator, 100))

print('test 9')

print(list(take([], 100)))