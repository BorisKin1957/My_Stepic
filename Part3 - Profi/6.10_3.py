'''
Функция get_value()

Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:

    chainmap — объект типа ChainMap, элементами которого являются словари
    key — произвольный объект
    from_left — булево значение, по умолчанию равное True

Функция должна возвращать значение по ключу key из chainmap, причем:

    если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
    если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому

Если ключ key отсутствует в chainmap, функция должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_value(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

Sample Output 1:

Arthur

Sample Input 2:

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

Sample Output 2:

Timur

Sample Input 3:

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))

Sample Output 3:

None

'''

def get_value(ch, key, left=True):
    if key in ch:
        if not left:
            ch = ch.maps[-1:][0]
        return ch[key]

from collections import ChainMap


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))