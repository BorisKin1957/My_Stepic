'''Функция get_days_in_month()

Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:

    year — натуральное число
    month — полное название месяца на английском

Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

Примечание 1. Например, вызов:
get_days_in_month(2021, 'December')

должен вернуть список:
[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ...,
datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
функцию get_days_in_month(), но не код, вызывающий ее.'''

def get_days_in_month(year, month):
    result = []
    ind = list(calendar.month_name).index(month)
    len_month = calendar.monthrange(year, ind)[1]
    for i in range(1, len_month + 1):
        dt = date(year, ind, i)
        result.append(dt)

    return (result)


import calendar
from datetime import date

print(get_days_in_month(2021, 'December'))