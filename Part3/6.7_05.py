'''
The Zen of Python

Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...

Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте.
Буквы и их количество должны выводиться в лексикографическом порядке, каждая на отдельной строке,
в следующем формате:

<буква>: <количество>

Примечание 1. Начальная часть ответа выглядит так:

a: 53
b: 21
...

Примечание 2. Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.

Примечание 3. Программа должна игнорировать все небуквенные символы.

Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''

from collections import Counter

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    txt = file.read().lower()

for char in txt:
    if ord(char) < 97 or ord(char) > 122:
        txt = txt.replace(char, '')

counter = Counter(txt)

all = sorted(counter.items(), key=lambda x: x[0])

for key, value in all:
    print(f'{key}: {value}')