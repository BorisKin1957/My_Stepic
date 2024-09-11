'''
Я в аду?

Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:

7-ddd-ddd-dd-dd

8-ddd-dddd-dddd

где d — цифра от 00 до 99.

Формат входных данных
На вход программе подается строка произвольного содержания.

Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам,
указанным в условии задачи, и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке.

Примечание. Тестовые данные доступны по ссылкам:


Sample Input 1:

Перезвони мне, пожалуйста: 7-919-667-21-19

Sample Output 1:

7-919-667-21-19

Sample Input 2:

Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911

Sample Output 2:

7-919-667-21-19
8-917-4864-1911

'''

def is_phone_number(phone):
    groups = phone.split('-')
    tmp = list(map(lambda x: len(str(x)), groups))
    if groups[0] != '7' and groups[0] != '8' or (tmp != [1, 3, 3, 2, 2] and tmp != [1, 3, 4, 4]):
        return False
    chars = ''.join(groups)
    return all(c.isdigit() for c in chars)

def get_all_numbers(text):
    L = []
    for c in range(len(text)):
        chunk = text[c:c + 15]
        if is_phone_number(chunk):
            if '7' + chunk[1:] not in L and '8' + chunk[1:] not in L:
                L.append(chunk)
    return L

string = input()

print(*(i for i in get_all_numbers(string)), sep='\n')
