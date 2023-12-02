'''Функция is_rising()

Реализуйте функцию is_rising(), которая принимает один аргумент:

    iterable — итерируемый объект, элементами которого являются числа

Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию,
или False в противном случае.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством,
а также содержит не менее двух элементов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_rising(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(is_rising([1, 2, 3, 4, 5]))

Sample Output 1:

True

Sample Input 2:

iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

Sample Output 2:

False

Sample Input 3:

iterator = iter(list(range(100, 200)))

print(is_rising(iterator))

Sample Output 3:

True

Верно решили 979 учащихся
Из всех попыток 74% верных
Хорошая работа. '''


def is_rising(iterable):
    new = iter(iterable)
    prew, last = next(new), next(new)
    try:
        while prew < last:
            flag = True
            prew, last = last, next(new)
        else:
            flag = False
    except:
        pass
    return flag

'''НАДО ТАК:

from itertools import pairwise

def is_rising(iterable):
    for a, b in pairwise(iterable):
        if a >= b:
            return False
    return True



'''


print(is_rising([1, 2, 3, 4, 5]))

print('test 2')

iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

print('test 3')

iterator = iter(list(range(100, 200)))

print(is_rising(iterator))

print('test 4')

iterator = iter(list(range(200, 100, -1)))

print(is_rising(iterator))

print('test 5')

iterator = iter(list(range(100, 201)) + [200])

print(is_rising(iterator))

print('test 6')

iterator = iter([10]*50)

print(is_rising(iterator))