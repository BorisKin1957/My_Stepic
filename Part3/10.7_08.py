'''
Функция unique()

Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без дубликатов.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию unique(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))

Sample Output 1:

1 2 3 4 5

Sample Input 2:

iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))

Sample Output 2:

1
2
3

'''


def unique(iterable):
    # l = []
    # for i in iterable:
    #     if i not in l:
    #         l.append(i)
    # l = []
    # no = [l.append(i) for i in iterable if i not in l]
    # yield from l

    numbers = [1, 2, 2, 3, 4, 5, 5, 5]

    print(*unique(numbers))

    print('test 2')

    iterator = iter('111222333')
    uniques = unique(iterator)

    print(next(uniques))
    print(next(uniques))
    print(next(uniques))

    print('test 3')

    data = map(abs, range(-100, 100))

    print(*unique(data))

    print('test 4')

    data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

    print(*unique(data))

    print('test 5')

    data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

    print(*unique(data))

    print('test 6')

    data = map(str.lower, 'STEPIK')

    print(*unique(data))

    print('test 7')

    data = map(str.lower, 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

    print(*unique(data))

    print('test 8')

    data = ['bee', 'geek', 'stepik', 'python']

    print(*unique(data))

    print('test 9')

    print(list(unique([])))