'''
Функция abbreviate()

Аббревиатура — слово, образованное сокращением слова или словосочетания и читаемое по алфавитному
названию начальных букв или по начальным звукам слов, входящих в него.

Реализуйте функцию abbreviate(), которая принимает один аргумент:

    phrase — фраза

Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.



Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию abbreviate(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(abbreviate('javaScript object notation'))

Sample Output 1:

JSON

Sample Input 2:

print(abbreviate('frequently asked questions'))

Sample Output 2:

FAQ

Sample Input 3:

print(abbreviate('JS game sec'))

Sample Output 3:

JSGS

Верно решили 950 учащихся
Из всех попыток 75% верных
Абсолютно точно. '''

import re

def abbreviate(phrase):
    L = []
    new = re.findall(r'\b\w*[A-Z]|\b\w', phrase)
    for i in new:
        if len(i) > 1:
            L.append(i[0] + i[-1])
        else:
            L.append(i)
    return ''.join(L).upper()

'''НАДО БЫЛО:

def abbreviate(phrase):
    return ''.join(re.findall(r'[A-Z]|\b\w',phrase)).upper()
'''