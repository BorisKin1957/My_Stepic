'''
Одинаковые слоги

Напишите программу, которая выводит слова, состоящие из двух одинаковых слогов.

Формат входных данных
На вход программе подается произвольное количество слов, каждое на отдельной строке.

Формат выходных данных
Программа должна из введенных слов вывести только те, которые состоят из двух одинаковых слогов.
Слова должны быть расположены в своем исходном порядке, каждое на отдельной строке.

Примечание 1. Словом будем считать любую непрерывную последовательность из одного или нескольких символов, соответствующих \w.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

Python
beebee
PyPy
portal

Sample Output 1:

beebee
PyPy

Sample Input 2:

gogo
hohoho
XaXaXaXa

Sample Output 2:

gogo
XaXaXaXa

Верно решили 950 учащихся
Из всех попыток 61% верных
Отличное решение! '''

# import sys
#
# for line in sys.stdin:
#     word = line.strip()
#     if len(word) % 2 == 0:
#         h = int(len(word) / 2)
#         begin = word[:h]
#         end = word[h:]
#         if begin == end:
#             print(word)

import sys
from re import search

for line in sys.stdin:
    word = line.strip()
    if len(word) % 2 == 0:
        h = int(len(word) / 2)
        word = word[:h] + ',' + word[h:]
        m = search('(\w+),(\w+)', word)
        if m.group(1) == m.group(2):
            print(m.group(1)+ m.group(2))