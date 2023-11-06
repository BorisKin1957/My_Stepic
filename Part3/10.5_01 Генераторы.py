'''
Функция simple_sequence()

Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность натуральных чисел,
в которой каждое число встречается столько раз, каково оно:
1,2,2,3,3,3,4,4,4,4,..
1,2,2,3,3,3,4,4,4,4,..Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную
функцию simple_sequence(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

generator = simple_sequence()

print(next(generator))
print(next(generator))

Sample Output 1:

1
2

Sample Input 2:

generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)

Sample Output 2:

1 2 2 3 3 3 4 4 4 4


Верно решили 937 учащихся
Из всех попыток 88% верных
Правильно, молодец! '''

'''КОРОЧЕ

def simple_sequence():
    number = 1
    while True:
        for _ in range(number):
            yield number
        number += 1

'''


def simple_sequence():
    value = 1
    index = 1
    while True:
        for i in range(index):
            yield value
        index += 1
        value += 1


generator = simple_sequence()

print(next(generator))
print(next(generator))
print(next(generator))

print('test 2')

generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)

print('test 3')

generator = simple_sequence()

for _ in range(100):
    print(next(generator))

print('test 4')

generator = simple_sequence()

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print('test 5')

generator = simple_sequence()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print('test 6')

generator = simple_sequence()

for _ in range(10_000_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))