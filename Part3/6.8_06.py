'''

Вам доступна переменная data, содержащая Counter словарь. Дополните приведенный ниже код,
чтобы он добавил этому словарю два атрибута:

    min_values() — функция, которая возвращает список элементов, имеющих наименьшее значение
    max_values() — функция, которая возвращает список элементов, имеющих наибольшее значение

Обе функции не должны принимать никаких аргументов.

Примечание 1. Элементом словаря будем считать кортеж (ключ, значение).

Примечание 2. Элементы словаря в возвращаемых функциями списках должны располагаться в своем исходном порядке.

Примечание 3. Функции data.min_values() и data.max_values() должны учитывать содержимое словаря.
Например, если в словарь data будет добавлена новая пара ключ-значение, то и в возвращаемых функциями
списках данные ключ и значение должны присутствовать.

Примечание 4. Программа ничего не должна выводить.

Примечание 5. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(data.max_values())

Sample Output 1:

[('j', 8), ('q', 8)]

Sample Input 2:

print(data.min_values())

Sample Output 2:

[('t', 1)]

'''

from collections import Counter


def fun_max_values():
    dat = sorted(data.items(), key=lambda x: -x[1])
    k, L = dat[0][1], []

    for i in dat:
        if i[1] == k:
            L.append(i)

    return L


def fun_min_values():
    dat = sorted(data.items(), key=lambda x: x[1])
    k, L = dat[0][1], []

    for i in dat:
        if i[1] == k:
            L.append(i)

    return L


data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.max_values = fun_max_values
data.min_values = fun_min_values

data['t'] += 1

clue = [('b', 2), ('c', 2), ('n', 2), ('t', 2)]
reply = data.min_values()

print(type(reply))
print(set(reply) == set(clue))