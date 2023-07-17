'''Функция get_all_values()

Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

    chainmap — объект типа ChainMap, элементами которого являются словари
    key — произвольный объект

Функция должна возвращать множество, элементами которого являются все значения по ключу key
из всех словарей в chainmap. Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.

Примечание 1. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит словари с
хешируемыми значениями.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_values(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))

Sample Output 1:

Arthur Timur

Sample Input 2:

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)

Sample Output 2:

set()

'''


def get_all_values(ch, name):
    result = set()
    while name in ch:
        result.add(ch[name])
        ch = ch.parents
    return result


from collections import ChainMap

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))
