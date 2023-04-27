'''Функция spell()

Реализуйте функцию spell(), которая принимает произвольное количество позиционных
аргументов-слов и возвращает словарь, ключи которого — первые буквы слов,
а значения — максимальные длины слов на эту букву.

Примечание 1. Если в функцию не передается ни одного аргумента, функция
должна возвращать пустой словарь.

Примечание 2. Функция должна игнорировать регистр слов, при этом в
результирующий словарь должны попасть именно буквы в нижнем регистре.

Input 1:
words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))

Sample Output 1:
{'р': 7, 'а': 9, 'у': 10, 'к': 5}

Sample Input 2:
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

Sample Output 2:
{'м': 10, 'и': 11, 'х': 5, 'б': 8}

'''

def spell(*args):
    new = [word.lower() for word in args]
    resalt = {}
    for word in new:
        key = word[0]
        k_filtered_new = filter(lambda i: i[0] == key, new) # список лишь из слов на букву key
        len_new = sorted(k_filtered_new, key=len)           # сортируем его по длине слова
        resalt[key] = resalt.get(key, len(len_new[-1]))     # длина последнего слова в списке - значение по ключу key
    return resalt

words = ['a', 'ab', 'abc', 'abcd', 'ба', 'аб', 'абвгдеЁёёЁЁжбБбБввВ', 'ёёё', 'Ёаaа']
print(spell(*words))

'''КРАСИВОЕ:

def spell(*args):
    result = {}
    for word in args:
        if result.get(word[0].lower(), 0) < len(word):
            result[word[0].lower()] = len(word)
    return result

'''