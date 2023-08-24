'''
Функция remove_marks()

Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:

    text — произвольная строка
    marks — набор символов

Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.

Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию remove_marks(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)

Sample Output 1:

Hi Will we go together
1

Sample Input 2:

marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)

Sample Output 2:

Are you listening? Meet my family! There are my parents, my brother and me
Are you listening? Meet my family! There are my parents my brother and me.
Are you listening? Meet my family There are my parents, my brother and me.
Are you listening Meet my family! There are my parents, my brother and me.
4


Всё правильно. '''


def remove_marks(text, chars):
    remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1
    result = ''
    for i in text:
        if i not in chars:
            result += i
    return result


marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)