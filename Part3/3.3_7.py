'''Функция is_available_date() 🌶️

Во время визита очередного гостя сотрудникам отеля приходится проверять,
доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

    booked_dates — список строковых дат, недоступных для бронирования.
    Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:

    ['04.11.2021', '05.11.2021-09.11.2021']

    date_for_booking — одиночная строковая дата или период (две даты через дефис),
    на которую гость желает забронировать номер. Например:

    '01.11.2021' или '01.11.2021-04.11.2021'

Функция is_available_date() должна возвращать True, если дата или период date_for_booking
полностью доступна для бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию
is_available_date(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:


Sample Input 1:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

Sample Output 1:
True

Sample Input 2:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

Sample Output 2:
False'''

def is_available_date(dates, some_date):
# по типу входных данных вызываем функцию, которая вернет список отдельных дней
    if type(dates) == list:
        bad_days = list_day_from_list(dates) # список недоступных дней
    else:
        bad_days = list_date_from_s(dates)
    if type(some_date) == list:
        need_days = list_day_from_list(some_date) # список требуемых дней
    else:
        need_days = list_date_from_s(some_date)
# просматривая список требуемых дней, смотрим, не входит ли он в список недоступных дней
    for need_day in need_days:
        if need_day in bad_days:
            return False
    return True

# возвращаем список отдельных дней из общего списка дней
def list_day_from_list(dates):
    all_days = []
    pattern = '%d.%m.%Y'
    for i in dates:
        if len(i) == 10:
            one_day =  datetime.strptime(i, pattern)
            all_days.append(one_day)
        else:
            for j in list_date_from_s(i):
                all_days.append(j)
    return all_days

# возвращаем список дней из строки с днями (днем)
def list_date_from_s(s):
    pattern = '%d.%m.%Y'
    if len(s) == 10:
        return [datetime.strptime(s, pattern)]
    else:
        l = s.split('-')
        new = []
        first = datetime.strptime(l[0], pattern)
        last = datetime.strptime(l[1], pattern)
        next_day = datetime.fromtimestamp(first.timestamp() + 24 * 60 * 60)
        new.append(first)
        new.append(next_day)
        k = 2
        while next_day != last:
            next_day = datetime.fromtimestamp(first.timestamp() + k * (24 * 60 * 60))
            new.append(next_day)
            k += 1
        return new

from datetime import datetime

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.12.2021-08.12.2021'
print(is_available_date(dates, some_date))