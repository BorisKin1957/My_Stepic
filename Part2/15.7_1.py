'''Требовалось написать программу, которая:

    преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
    фильтрует список words  и оставляет только палиндромы длиной более 44 символов;
    находит произведение чисел из списка numbers.

Программист торопился и написал программу неправильно. Доработайте его программу.


[18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1, 1171.7, 146.9, 21.8, 6.0, 86.9]
['racecar', 'civic', 'TATTARRATTAT', 'malayalam']
24840

'''

from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda num: round(num ** 2, 1), floats))
filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)