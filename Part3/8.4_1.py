'''
Функция recursive_sum()

Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:

    nested_lists — список, элементами которого являются целые числа или списки, элементами которых,
    в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной

Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат.
Если список nested_lists пуст, функция должна вернуть число 00.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))

Sample Output 1:

24

Sample Input 2:

my_list = []

print(recursive_sum(my_list))

Sample Output 2:

0

Отличное решение!

'''


def recursive_sum(data, L=[]):
    for l in data:
        if type(l) == int:
            L.append(l)
        else:
            recursive_sum(l)
    return sum(L)


my_list = [1, [2, 3], 4, [5, [6, 7]], 8]

print(recursive_sum(my_list))

'''ТАК

def recursive_sum(data):
    total = 0
    for l in data:
        if type(l) == int:
            total += l
        else:
            total += recursive_sum(l)
    return total
'''