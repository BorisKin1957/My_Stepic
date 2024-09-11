'''
Функция alternating_sequence()

Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

    count — натуральное число, по умолчанию имеет значение None

Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный знакочередующийся ряд натуральных чисел.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.

Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид:
1,−2,3,−4,5,−6,7,−8,9,−10,...
1,−2,3,−4,5,−6,7,−8,9,−10,...Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную  функцию alternating_sequence(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

generator = alternating_sequence()

print(next(generator))
print(next(generator))

Sample Output 1:

1
-2

Sample Input 2:

generator = alternating_sequence(10)

print(*generator)

Sample Output 2:

1 -2 3 -4 5 -6 7 -8 9 -10

Из всех попыток 58% верных
Здорово, всё верно. '''


def alternating_sequence(n=None):
    value = 1
    k = 1
    if n:
        for _ in range(n):
            yield k * value
            k = -k
            value = abs(value) + 1
    else:
        while True:
            yield k * value
            k = -k
            value = abs(value) + 1


generator = alternating_sequence()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print('test 2')

generator = alternating_sequence(10)

print(*generator)

print('test 3')

generator = alternating_sequence(100)

print(*generator)

print('test 4')

generator = alternating_sequence(50)

for _ in generator:
    pass

try:
    next(generator)
except StopIteration:
    print('Error')

print('test 5')

generator = alternating_sequence()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print('test 6')

generator = alternating_sequence()

for _ in range(10_124_421):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print('test 7')

generator = alternating_sequence(1)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')