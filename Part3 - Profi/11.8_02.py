'''
Функция normalize_whitespace()

Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:

    string — произвольная строка

Функция должна заменять все множественные пробелы в строке string на единственный пробел и возвращать полученный результат.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию normalize_whitespace(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(normalize_whitespace('AAAA                A                AAAA'))

Sample Output 1:

AAAA A AAAA

Sample Input 2:

print(normalize_whitespace('Тут нет лишних пробелов'))

Sample Output 2:

Тут нет лишних пробелов

Sample Input 3:

print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))

Sample Output 3:

Тут н е т л и шних пробелов

Напишите программу. Тестируется через stdin → stdout
Верно решили 969 учащихся
Из всех попыток 90% верных
Верно. '''

import re

def normalize_whitespace(text):
    result = re.sub(r'\s+', r' ', text)

    return result

print(normalize_whitespace('AAAA                A                AAAA'))

print('test 2')
print(normalize_whitespace('Тут нет лишних пробелов'))

print('test 3')
print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))

print('test 4')
print(normalize_whitespace('K L  L    O    I!  !  I OP    PPPppdj O   P'))

print('test 5')
print(normalize_whitespace('               '))

print('test 6')
print(normalize_whitespace('aaaaaaaaaaaaaaaaaaaaaaaaaa'))

print('test 7')
print(normalize_whitespace('Раз два  три   четыре    пять      шесть      '))
print('test 8')
print(normalize_whitespace('      Шесть-----пять    четыре***три  два+один'))

