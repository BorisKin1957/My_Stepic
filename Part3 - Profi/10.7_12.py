'''
Функция around()

Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей,
каждый из которых содержит очередной элемент итерируемого объекта iterable, а также предыдущий и следующий за ним элементы:

(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)

Для первого элемента предыдущим считается значение None, для последнего элемента следующим считается так же значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию around(),
 но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:


Sample Input 1:

numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

Sample Output 1:

(None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)

Sample Input 2:

iterator = iter('hey')

print(*around(iterator))

Sample Output 2:

(None, 'h', 'e') ('h', 'e', 'y') ('e', 'y', None)

'''


def around(iterable):
    if not iterable:
        return []
    else:
        if type(iterable) == map:
            l_map = list(iterable)
            new = iter(l_map)
        else:
            new = iter(iterable)
            l_map = ''
        try:
            i, l = 0, [(None, next(new), next(new))]
            while True:
                l.append((l[i][1], l[i][2], next(new)))
                i += 1
        except StopIteration:
            try:
                l.append((l[i][1], l[i][2], None))
                yield from l
            except UnboundLocalError:
                yield None, *l_map , None
            except StopIteration:
                yield None, next(new), None


numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

print('test 2')

iterator = iter('hey')

print(*around(iterator))

print('test 3')

iterator = around(iter('beegeek'))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print('test 4')

data = map(abs, range(-100, 100))

print(*around(data))

print('test 5')

data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*around(data))

print('test 6')

data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))

print('test 7')

data = map(str.upper, 'yt')

print(*around(data))

print('test 8')

data = map(str.upper, 'ytu')

print(*around(data))

print('test 9')

data = ['bee', 'geek', 'stepik', 'python']

print(*around(data))

print('test 10')

print(list(around([])))