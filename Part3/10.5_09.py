'''
Функция flatten()

Реализуйте генераторную функцию flatten(), которая принимает один аргумент:

    nested_list — список, элементами которого являются целые числа или списки, элементами которых,
    в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной

Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list, включая все числа
из всех вложенных списков, а затем возбуждает исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию flatten(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)

Sample Output 1:

1 2 3 4 5

Sample Input 2:

generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)

Sample Output 2:

1 2 3 4 5 6 7

Верно решили 938 учащихся
Из всех попыток 83% верных
Правильно, молодец! '''

def flatten(data):
    for elem in data:
        if type(elem) == int:
            yield elem
        else:
            yield from flatten(elem)


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)

print('test 2')

generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)

print('test 3')

generator = flatten([3, [4], [5, [6, [7, 8]]]])

print(*generator)

print('test 6')

generator = flatten([[1], [2], [3], [4], [5], [6], [7]])

print(*generator)

print('test 9')

generator = flatten([[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]])

print(*generator)

print('test 12')

generator = flatten([12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]])

print(*generator)