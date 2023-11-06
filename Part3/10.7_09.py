'''
Функция stop_on()

Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    obj — произвольный объект

Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable до тех пор,
пока не будет достигнут элемент, равный obj. Если итерируемый объект iterable не содержит ни одного элемента,
равного obj, генератор должен породить все элементы iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию stop_on(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))

Sample Output 1:

1 2 3

Sample Input 2:

iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))

Sample Output 2:

b e e g e e k

'''


def stop_on(iterable, obj):
    for i in iterable:
        if i != obj:
            yield i
        else:
            break

#    yield from (i for i in iterable if i != obj)

numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))

print('test 2')

iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))

print('test 3')

data = map(abs, range(-100, 100))

iterator = stop_on(data, 76)

print(*iterator)

print('test 4')

data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

iterator = stop_on(data, 'o')

print(*iterator)

print('test 5')

data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

iterator = stop_on(data, 'e')

print(*iterator)

print('test 6')

data = 'g'

iterator = stop_on(data, 'g')

print(*iterator)

print('test 7')

data = 'eeeeeeeeeeeeee'

iterator = stop_on(data, 'e')

print(*iterator)

print('test 8')

data = iter('qweretqwewerqweqwerewr')

iterator = stop_on(data, 'H')

print(*iterator)

print('test 9')

data = iter('beegeek')

iterator = stop_on(data, 'g')

print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print('Error')

print('test 10')

data = ['bee', 'geek', 'stepik', 'python']

print(*stop_on(data, 'stepik'))

print('test 11')

data = []

print(list(stop_on(data, 'stepik')))
