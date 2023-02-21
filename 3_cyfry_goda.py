
'''Печатает годы в которых 3 одинаковые цифры
Например 1911, 2022'''
def triada(year):
    result = False
    for i in range(10):
        if str(year).count(str(i)) == 3:
            result = True
            break
    return result


year_first = int(input('Введите начальный год: '))
year_last = int(input('Введите последний год: '))

for i in range(year_first, year_last):
    year = year_first + 1
    if triada(year):
        print(year)
    year_first = year