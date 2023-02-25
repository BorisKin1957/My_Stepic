def triada(year):
    w = str(year)
    result = False
    for i in range(len(w)):
        if len(w.replace(w[i], ' ').strip()) == 1:
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