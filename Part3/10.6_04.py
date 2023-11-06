'''
Функция interleave()

Реализуйте функцию interleave() с использованием генераторных выражений,
которая принимает произвольное количество позиционных аргументов, каждый из которых является последовательностью.

Функция должна возвращать генератор, порождающий каждый элемент всех переданных последовательностей:
сначала первый элемент первой последовательности, затем первый элемент второй последовательности,
и так далее; после второй элемент первой последовательности, затем второй элемент второй последовательности, и так далее.

Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину.
Например, объекты типа list, str, tuple являются последовательностями.

Примечание 2. Гарантируется, что все последовательности, передаваемые в функцию, имеют равные длины.

Примечание 3. Гарантируется, что в функцию всегда подается хотя бы одна последовательность.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию interleave(), но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(*interleave('bee', '123'))

Sample Output 1:

b 1 e 2 e 3

Sample Input 2:

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))

Sample Output 2:

1 1 1 2 4 8 3 9 27

'''

def interleave(*args):
    yield from (elem[i] for i in range(len(args[0])) for elem in args)



print(*interleave('bee', '123'))

print('test 2')

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))

print('test 3')

numbers1 = tuple(range(10))
numbers2 = list(range(10, 20))
numbers3 = tuple(range(20, 30))
numbers4 = tuple(range(30, 40))

print(*interleave(numbers1, numbers2, numbers3, numbers4))

print('test 4')

string = str(range(10, 50))

print(*interleave(string))

print('test 5')

numbers1 = tuple(range(38, 99, 7))
numbers2 = tuple(range(65, 114, 6))
string1 = 'BEEGEEKbe'
string2 = 'STEPIKste'
numbers3 = list(range(1, 170, 19))
numbers4 = list(range(2, 175, 20))

print(*interleave(numbers3, string2, numbers4, string1, numbers2, numbers1))