'''Функция get_all_mondays()

Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

    year — натуральное число

Функция должна возвращать отсортированный по возрастанию список
всех дат (тип date) года year, выпадающих на понедельник.

Примечание 1. Например, вызов:

get_all_mondays(2021)

должен вернуть список:

[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ...,
datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
функцию get_all_mondays(), но не код, вызывающий ее.'''

def get_all_mondays(year):
    result = []
    if calendar.isleap(year):
        len_year = 366
    else:
        len_year = 365
    for i in range(len_year):
        dt = date(year, 1, 1) + timedelta(days=i)
        if dt.weekday() == 0:
            result.append(dt)

    return (result)


import calendar
from datetime import date, timedelta

print(get_all_mondays(1353))