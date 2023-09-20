'''
Новый print

Напишите программу с использованием декоратора, которая переопределяет функцию print() так,
чтобы она печатала весь текст в верхнем регистре.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print('hi', 'there', end='!')

Sample Output 1:

HI THERE!

Sample Input 2:

print('are you in trouble?')

Sample Output 2:

ARE YOU IN TROUBLE?

Sample Input 3:

print(111, 222, 333, sep='xxx')

Sample Output 3:

111XXX222XXX333

Всё получилось! '''

def false_print(fun):
    def upper(*args, **kwargs):
        args = (str(i).upper() for i in args)
        D = {}
        for key, value in kwargs.items():
            value = str(value).upper()
            D.update({key: value})
        fun(*args, **D)

    return upper


true_print = print
print = false_print


@false_print
def print(*args, **kwargs):
    true_print(*args, **kwargs)


print('hi', 'there', end='!')
print()
print('are you in trouble?')
print(111, 222, 333, sep='xxx')