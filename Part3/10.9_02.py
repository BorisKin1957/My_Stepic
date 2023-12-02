'''
Функция drop_this()

Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    obj — произвольный объект

Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, начиная с элемента, не равного obj.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию drop_this(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))

Sample Output 1:

1 2 3

Sample Input 2:

iterator = iter('bbbbeebee')

print(*drop_this(iterator, 'b'))

Sample Output 2:

e e b e e

Sample Input 3:

iterator = iter('ssssssssssssssssssssssss')

print(list(drop_this(iterator, 's')))

Sample Output 3:

[]


Верно решил 981 учащийся
Из всех попыток 86% верных
Хорошая работа. '''

from itertools import dropwhile

def drop_this(iterable, obj):
    return iter(dropwhile(lambda x: x == obj, iterable))

numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))

print('test 2')

iterator = iter('bbbbeebee')

print(*drop_this(iterator, 'b'))

print('test 3')

iterator = iter('ssssssssssssssssssssssss')

print(list(drop_this(iterator, 's')))

print('test 4')

letters = drop_this(iter('stepik'), 'g')

print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))