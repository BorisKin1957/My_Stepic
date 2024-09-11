'''
Функция with_previous()

Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей,
каждый из которых содержит очередной элемент итерируемого объекта iterable, а также предшествующий ему элемент:

(<очередной элемент>, <предыдущий элемент>)

Для первого элемента предыдущим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию with_previous(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:


Sample Input 1:

numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))

Sample Output 1:

(1, None) (2, 1) (3, 2) (4, 3) (5, 4)

Sample Input 2:

iterator = iter('stepik')

print(*with_previous(iterator))

Sample Output 2:

('s', None) ('t', 's') ('e', 't') ('p', 'e') ('i', 'p') ('k', 'i')

'''


def with_previous(iterable):
    if not iterable:
        return []
    new = iter(iterable)
    i, l = 0, [(next(new), None)]
    try:
        while True:
            l.append((next(new), l[i][0]))
            i += 1
    except:
        yield from l


numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))

print('test 2')

iterator = iter('stepik')

print(*with_previous(iterator))

print('test 3')

print(*with_previous(map(abs, range(-100, 100))))

print('test 4')

print(*with_previous(map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')))

print('test 5')

print(*with_previous('JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'))

print('test 6')

print(*with_previous('A'))

print('test 7')

print(*with_previous('AB'))

print('test 8')

gen = with_previous(['bee', 'geek', 'stepik', 'python'])

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('test 9')

print(list(with_previous('')))