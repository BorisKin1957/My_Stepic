'''
Итератор DictItemsIterator

Как известно, во время итерации по словарю мы получаем ключи, а не значения или пары ключ-значение.

Приведенный ниже код:

info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}

print(*info)

выводит:

name age gender

Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:

    data — словарь

Итератор класса DictItemsIterator должен генерировать последовательность кортежей, представляющих
собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.

Примечание 1. При решении задачи не используйте словарные методы keys(), values() и items().

Примечание 2. Пары ключ-значение в возвращаемом функцией итераторе должны располагаться в своем изначальном порядке.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс DictItemsIterator.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)

Sample Output 1:

(1, 'A') (2, 'B') (3, 'C')

Sample Input 2:

data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)

Sample Output 2:

(1, 1) (2, 4) (3, 9) (4, 16) (5, 25) (6, 36) (7, 49)


Верно решили 940 учащихся
Из всех попыток 63% верных
Всё правильно. '''

class StopIteration(Exception):
    pass

class DictItemsIterator:
    def __init__(self, data):
        self.d = data
        self.l = list(self.d)
        self.v = []

    def __iter__(self):
        for i in range(len(self.l)):
            self.v.append((self.l[0], self.d[self.l[0]]))
            del self.l[0]
        return iter(self.v)

    def __next__(self):
        if self.l:
            value = (self.l[0], self.d[self.l[0]])
            del self.l[0]
            return value
        raise StopIteration('StopIteration')

'''ВОТ КАК!

class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        return key, self.data[key]
'''


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)

print('test 2')

data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)

print('test 3')

data = {'Arthur': 100, 'Timur': 100, 'Dima': 100,
        'Anri': 101, 'Roma': 99, 'German': 98}

pairs = DictItemsIterator(data)

print(list(pairs))

print('test 4')

data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8],
        'Anri': [100, 101], 'Roma': [99]}

pairs = DictItemsIterator(data)

print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')

print('test 5')

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

pairs = DictItemsIterator(data)

print(tuple(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')