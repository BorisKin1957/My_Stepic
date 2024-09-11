'''
Функция dates()

Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

    start — дата, тип date
    count — натуральное число, по умолчанию имеет значение None

Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность
из максимально допустимого количества дат (тип date), начиная с даты start.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор,
порождающий последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию dates(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))

Sample Output 1:

2022-03-08
2022-03-09
2022-03-10

Sample Input 2:

generator = dates(date(2022, 3, 8), 5)

print(*generator)

Sample Output 2:

2022-03-08 2022-03-09 2022-03-10 2022-03-11 2022-03-12


Верно решили 899 учащихся
Из всех попыток 28% верных
Так точно! '''

from datetime import date

def dates(start, count=None):
    begin = date.toordinal(start)
    if count:
        end = begin + count
    else:
        end = date.toordinal(date(9999, 12, 31)) + 1
    for day_number in range(begin, end):
        yield date.fromordinal(day_number)

generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))

print('test 2')

generator = dates(date(2022, 3, 8), 5)

print(*generator)

print('test 3')

generator = dates(date(2025, 9, 11), 99)

print(*generator)

print('test 4')

generator = dates(date(2024, 9, 13), 1)

try:
    d = next(generator)
    print(type(d))
    print(d)
    next(generator)
except StopIteration:
    print('Error')

print('test 5')

generator = dates(date(2049, 1, 7))

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
print(next(generator))

print('test 6')

generator = dates(date(9999, 1, 7))

for _ in range(348):
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
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')