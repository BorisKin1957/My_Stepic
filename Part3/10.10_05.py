'''
Функция grouper()

Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные
в кортежи по n элементов соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей,
то ими становится значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию grouper(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))

Sample Output 1:

(1, 2) (3, 4) (5, 6)

Sample Input 2:

iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))

Sample Output 2:

(1, 2, 3) (4, 5, 6) (7, None, None)

Sample Input 3:

iterator = iter([1, 2, 3])

print(*grouper(iterator, 5))

Sample Output 3:

(1, 2, 3, None, None)

Верно решили 902 учащихся
Из всех попыток 73% верных
Хорошие новости, верно! '''

def grouper(iterable, n):
    result, L, iter1 = [], [0], iter(iterable)
    while L[0] != None:
        L = []
        for i in range(n):
            L.append(next(iter1, None))
        if L[0] != None:
            result.append(tuple(L))
    return result

'''ПРАВИЛЬНО:

from itertools import repeat, zip_longest

def grouper(iterable, n):
    return zip_longest(*repeat(iter(iterable), n))

'''


numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))

print('test 2')

iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))

print('test 3')

iterator = iter([1, 2, 3])

print(*grouper(iterator, 5))

print('test 4')

iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 4))

print('test 5')

iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 5))

print('test 6')

iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 1))

print('test 7')

iterator = iter('beegeek')

print(*grouper(iterator, 5))

print('test 8')

iterator = iter('beegeek')

print(*grouper(iterator, 20))