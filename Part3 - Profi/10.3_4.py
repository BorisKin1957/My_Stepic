'''
Функция random_numbers()

Реализуйте функцию random_numbers(), которая принимает два аргумента:

    left — целое число
    right — целое число

Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел в диапазоне
от left до right включительно.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый итератор random_numbers(),
но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))

Sample Output 1:

1
1

Sample Input 2:

iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

Sample Output 2:

True
True
True


Верно решили 940 учащихся
Из всех попыток 75% верных
Всё правильно. '''

from random import choice


def random_numbers(start, stop):
    return iter(lambda: choice(range(start, stop + 1)), None)

iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))

print('2')

iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

print('test 4')

iterator = random_numbers(5, 5)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print('test 5')

iterator = random_numbers(1000, 1001)

print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))

print('6')

iterator = random_numbers(-100, 99)

print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))