'''Функция print_good_dates()

Тимур считает дату «интересной», если её год совпадает с годом его рождения,
а сумма номера месяца и номера дня равна его возрасту.
Год рождения Тимура — 1992, возраст — 29 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:

    dates — список дат (тип date)

Функция должна выводить «интересные» даты в порядке возрастания,
каждую на отдельной строке, в формате  month_name DD, YYYY,
где month_name — полное название месяца на английском.

Примечание 1. Если в функцию передается пустой список или список без
интересных дат, функция ничего не должна выводить.

Примечание 2. В тестирующую систему сдайте программу, содержащую только
необходимую функцию print_good_dates(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Sample Input 1:
dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

Sample Output 1:
September 20, 1992
October 19, 1992'''

def print_good_dates(dates):
    birthday = []
    for day in dates:
        if day.year == 1992 and day.month + day.day == 29:
            birthday.append(day)
    if birthday:
        birthday = sorted(birthday)
        print(*[day.strftime('%B %d, %Y') for day in birthday], sep='\n')


from datetime import date

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)