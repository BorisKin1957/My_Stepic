'''
Функция ncycles()

Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    times — натуральное число

Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, зацикленных times раз.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию ncycles(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(*ncycles([1, 2, 3, 4], 3))

Sample Output 1:

1 2 3 4 1 2 3 4 1 2 3 4

Sample Input 2:

iterator = iter('bee')

print(*ncycles(iterator, 4))

Sample Output 2:

b e e b e e b e e b e e

Sample Input 3:

iterator = iter([1])

print(*ncycles(iterator, 10))

Sample Output 3:

1 1 1 1 1 1 1 1 1 1

Верно решили 965 учащихся
Из всех попыток 78% верных
Так точно! '''

from itertools import tee, chain

def ncycles(iterable, times):
    return chain(*tee(iterable, times))
#   return chain.from_iterable(tee(iterable, times)


print(*ncycles([1, 2, 3, 4], 3))

print('test 2')

iterator = iter('bee')

print(*ncycles(iterator, 4))

print('test 3')

iterator = iter([1])

print(*ncycles(iterator, 10))