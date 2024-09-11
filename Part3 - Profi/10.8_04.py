'''
Функция roundrobin() 🌶️

Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов,
каждый из которых является итерируемым объектом.

Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных
итерируемых объектов: сначала первый элемент первого итерируемого объекта,
затем первый элемент второго итерируемого объекта, и так далее; после второй элемент первого итерируемого объекта,
затем второй элемент второго итерируемого объекта, и так далее.

Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться
в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию roundrobin(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(*roundrobin('abc', 'd', 'ef'))

Sample Output 1:

a d e b f c

Sample Input 2:

numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))

Sample Output 2:

1 b 2 e 3 e g e e k

Sample Input 3:

print(list(roundrobin()))

Sample Output 3:

[]

Верно решили 868 учащихся
Из всех попыток 42% верных
Правильно. '''

def roundrobin(*iterable):
    if not iterable:
        return []
    j = 0
    l = [iter(elem) for elem in iterable]
    while j < 100:
        for i in l:
            try:
                yield next(i)
            except StopIteration:
                j += 1
                continue


print(*roundrobin('abc', 'd', 'ef'))

print('test 2')

numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))

print('test 3')

print(list(roundrobin()))

print('test 4')

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = range(5)
letters = iter('beegeek')

print(*roundrobin(numbers1, numbers2, letters))

print('test 5')

letters = iter('stepik')

print(*roundrobin(letters))

print('test 6')

numbers = roundrobin(map(abs, range(-10, 10)))

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

print('test 7')

numbers1 = map(abs, range(-10, 10))
numbers2 = filter(None, range(-10, 10))
numbers3 = map(abs, range(-5, 5))
numbers4 = filter(None, range(-5, 5))
numbers5 = map(abs, range(-1, 1))
numbers6 = filter(None, range(-1, 1))

print(*roundrobin(numbers1, numbers2, numbers3, numbers4, numbers5, numbers6))

print('test 8')

print(list(roundrobin([], [], [], [])))

print('tedt 9')

numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))