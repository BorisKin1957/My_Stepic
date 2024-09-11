'''
Итератор RandomNumbers

Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

    left — целое число
    right — целое число
    n — натуральное число

Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел от left до right включительно,
а затем возбуждать исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс RandomNumbers.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

Sample Output 1:

1
1
1

Sample Input 2:

iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

Sample Output 2:

True
True

Верно решили 935 учащихся
Из всех попыток 71% верных
Всё получилось! '''


import random



class RandomNumbers:
    def __init__(self, left, right, n):
        L = []
        for i in range(n):
            L.append(random.randint(left, right))
        self.iterator = iter(L)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator:
            return next(self.iterator)
        raise StopIteration

iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

print('test 4')

iterator = RandomNumbers(5, 5, 98)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print('test 8')

iterator = RandomNumbers(-1000, -900, 4)

print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')


