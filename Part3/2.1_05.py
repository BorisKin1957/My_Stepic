'''Функция convert()

Реализуйте функцию convert(), которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать строку string:

    полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
    полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
    полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает

Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.

Sample Input 1:
print(convert('BEEgeek'))

Sample Output 1:
beegeek

Sample Input 2:
print(convert('pyTHON'))

Sample Output 2:
PYTHON

Sample Input 3:
print(convert('pi31415!'))

Sample Output 3:
pi31415!

'''


def convert(string):
    small, big = 0, 0
    for i in string:
        if i.islower():
            small += 1
        elif i.isupper():
            big += 1
    if small >= big:
        return string.lower()
    else:
        return string.upper()

print(convert('pi31415!'))