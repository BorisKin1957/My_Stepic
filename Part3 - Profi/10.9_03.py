'''
Функция first_true()

Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()

Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable,
для которого функция predicate вернула значение True. Если такого элемента нет,
функция first_true() должна вернуть значение None.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного
в качестве аргумента значения.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_true(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Sample Input 1:

numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))

Sample Output 1:

2

Sample Input 2:

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))

Sample Output 2:

100

Sample Input 3:

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))

Sample Output 3:

69

Верно решили 967 учащихся
Из всех попыток 51% верных
Всё получилось! '''

def first_true(iterable, predicate):
    try:
        return next(filter(predicate, iterable))
    except StopIteration:
        return None
'''КОРОЧЕ
в next можно передавать второй параметр, который будет возвращаться вместо возбуждения исключения

def first_true(iterable, predicate):
        return next(filter(predicate, iterable), None)
'''

numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))

print('test 2')

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))

print('test 3')

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))


print('test 4')

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))

print('test 5')

numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 0))

print('test 6')

numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 1))

print('test 7')

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num == 200))

print('test 8')

numbers = iter([])

print(first_true(numbers, lambda num: num == 200))