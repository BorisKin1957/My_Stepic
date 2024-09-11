'''
Функция filter_names()

Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:

    names — список имен
    ignore_char — одиночный символ
    max_names — натуральное число

Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые

    начинаются на ignore_char (в любом регистре)
    содержат хотя бы одну цифру

Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка.

Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_names(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Sample Input 1:

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))

Sample Output 1:

Timur Arthur Arina

Sample Input 2:

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))

Sample Output 2:

Dima Arthur Arina German Ruslan

Sample Input 3:

data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))

Sample Output 3:

Верно решили 953 учащихся
Из всех попыток 59% верных
Правильно. '''


def filter_names(names, ignore_char, max_names):
    if len(names) < max_names:
        max_names = len(names)
    count = -1
    for name in names:
        count += 1
        if name[0].lower() != ignore_char.lower() and name.isalpha() and count < max_names:
            yield name
        else:
            count -= 1


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))

print('test 2')

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))

print('test 3')

data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))