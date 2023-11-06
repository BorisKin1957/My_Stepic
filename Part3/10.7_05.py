'''
Функция years_days()

Реализуйте генераторную функцию years_days(), которая принимает один аргумент:

    year — натуральное число

Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.

Примечание 1. Возьмем в качестве примера 2022 год. В январе этого года 31 день, в феврале — 28, в марте — 31, и так далее.
Тогда генератор, полученный при вызове years_days(2022), должен порождать сначала все даты с 1 по 31 января, затем с 1 по 28 февраля,

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию years_days(),
но не код, вызывающий ее.

Sample Input:

dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

Sample Output:

2022-01-01
2022-01-02
2022-01-03
2022-01-04

'''


from datetime import date

def years_days(year):
    start = date(year, 1, 1).toordinal()
    end = date(year, 12, 31).toordinal() + 1
    yield from (date.fromordinal(day_number) for day_number in range(start, end))



dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

print('test 2')

dates = years_days(2077)

print(*dates)

print('test 3')

dates = years_days(2000)

print(*dates)

print('test 4')

dates = years_days(1900)

print(*dates)