'''
Функция primes()

Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:

    left — натуральное число
    right — натуральное число

Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно,
а затем возбуждающий исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.
Единица простым числом не является.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию primes(),
 но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

generator = primes(1, 15)

print(*generator)

Sample Output 1:

2 3 5 7 11 13

Sample Input 2:

generator = primes(6, 36)

print(next(generator))
print(next(generator))

Sample Output 2:

7
11


Верно решили 937 учащихся
Из всех попыток 60% верных
Прекрасный ответ. '''

def primes(left, right):
    for value in range(left, right + 1):
        flag = True
        for i in range(2, value):           # перебираю делители
            if value % i == 0:
                flag = False
        if flag and value > 1:
            yield value
generator = primes(1, 15)

print(*generator)

print('test 2')

generator = primes(6, 36)

print(next(generator))
print(next(generator))

print('test 3')

generator = primes(37, 37)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')

print('test 4')

generator = primes(39, 83)

print(*generator)

print('test 5')

generator = primes(43, 79)

print(*generator)

print('test 6')

generator = primes(43, 72)

print(*generator)

print('test 7')

generator = primes(1000, 2000)

print(*generator)

print('test 8')

generator = primes(2000, 100000)

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))