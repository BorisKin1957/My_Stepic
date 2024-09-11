'''
Функция max_pair()

Реализуйте функцию max_pair(), которая принимает один аргумент:

    iterable — итерируемый объект, элементами которого являются числа

Функция должна возвращать единственное число — максимальную сумму двух соседних чисел итерируемого объекта iterable.

Примечание 1. Рассмотрим список чисел 1,8,2,4,31,8,2,4,3 из первого теста.
Из данной последовательности можно получить следующие пары соседних элементов: 11 и 88, 88 и 22, 22 и 44, 44 и 33.
Максимальную сумму имеет вторая пара — 1010.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством,
а также содержит не менее двух элементов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию max_pair(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(max_pair([1, 8, 2, 4, 3]))

Sample Output 1:

10

Sample Input 2:

iterator = iter([1, 2, 3, 4, 5])

print(max_pair(iterator))

Sample Output 2:

9

Sample Input 3:

iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(max_pair(iterator))

Sample Output 3:

0

Верно решили 978 учащихся
Из всех попыток 89% верных
Правильно, молодец! '''

from itertools import pairwise, chain

def max_pair(iterable):
    new = iter(pairwise(iterable))
    result = sum(next(new))
    for i in(chain(new)):
        if sum(i) > result:
            result = sum(i)
    return result


print(max_pair([1, 8, 2, 4, 3]))

print('test 2')

iterator = iter([1, 2, 3, 4, 5])

print(max_pair(iterator))

print('test 3')

iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(max_pair(iterator))