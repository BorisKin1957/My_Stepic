'''
Функция pairwise()

Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит
очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:

(<очередной элемент>, <следующий элемент>)

Для последнего элемента следующим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию pairwise(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Sample Input 1:

numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

Sample Output 1:

(1, 2) (2, 3) (3, 4) (4, 5) (5, None)

Sample Input 2:

iterator = iter('stepik')

print(*pairwise(iterator))

Sample Output 2:

('s', 't') ('t', 'e') ('e', 'p') ('p', 'i') ('i', 'k') ('k', None)

Sample Input 3:

print(list(pairwise([])))

Sample Output 3:

[]

'''

def pairwise(iterable):
    if not iterable:
        return []
    i, new = 0, iter(iterable)
    try:
        l = [(next(new), next(new))]
    except StopIteration:
        yield (iterable, None)
    try:
        while True:
            l.append((l[i][1], next(new)))
            i += 1
    except StopIteration:
        l.append((l[i][1], None))
        yield from l


numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

print('test 2')

iterator = iter('stepik')

print(*pairwise(iterator))

print('test 3')

print(list(pairwise([])))

print('test 4')

data = map(abs, range(-100, 100))

print(*pairwise(data))

print('test 5')

data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*pairwise(data))

print('test 6')

data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*pairwise(data))

print('test 7')

iterator = pairwise('A')

print(next(iterator))

print('test 8')

data = ['bee', 'geek', 'stepik', 'python']

print(*pairwise(data))

'''ЛУЧШЕЕ

def pairwise(iterable):
    it = iter(iterable)
    i = next(it, None)
    while i != None:
        i, prev = next(it, None), i
        yield prev, i
'''

