'''
Функция all_together()

Реализуйте функцию all_together() с использованием генераторных выражений,
которая принимает произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

Функция должна возвращать генератор, порождающий каждый элемент всех переданных итерируемых объектов:
сначала все элементы первого итерируемого объекта, затем второго, и так далее.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию all_together(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))

Sample Output 1:

0 1 2 b e e 1 3 5 2 4 6

Sample Input 2:

objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]

print(*all_together(*objects))

Sample Output 2:

1 2 3 (0, 0) (1, 1) geek

Sample Input 3:

print(list(all_together()))

Sample Output 3:

[]


Верно решили 977 учащихся
Из всех попыток 87% верных
Правильно. '''

def all_together(*args):
    for elem in args:
        yield from (i for i in elem)


objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))

print('test 2')

objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]

print(*all_together(*objects))

print('test 3')

print(list(all_together()))

print('test 4')

objects = [iter('bee'), [[1, 2], [3, 4], [5, 6]], {'geek': 1, 'bee': 2}]

print(*all_together(*objects))

print('test 5')

_map = map(str.upper, 'beegeek')
_filter = filter(str.islower, 'BEEgeek')
_zip = zip('bee', '123')

print(*all_together(_map, _filter, _zip))