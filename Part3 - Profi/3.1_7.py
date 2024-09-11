'''Функция saturdays_between_two_dates()

Реализуйте функцию saturdays_between_two_dates(), которая принимает
два аргумента в следующем порядке:

    start — начальная дата, тип date
    end — конечная дата, тип date

Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется,
что первая дата меньше второй.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
функцию saturdays_between_two_dates(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:



Sample Input 1:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))

Sample Output 1:
3

Sample Input 2:
date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)
print(saturdays_between_two_dates(date1, date2))

Sample Output 2:
4

'''

def saturdays_between_two_dates(date1, date2):
    date_list, count = [date1, date2], 0
    for day in range(min(date_list).toordinal(), max(date_list).toordinal() + 1):
        if date.fromordinal(day).weekday() == 5:
            count += 1
    return count


from datetime import date

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))