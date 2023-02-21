'''Печатает годы в которых 3 одинаковые цифры
Например 1911, 2022'''

def triada(year):
    count = 0
    w = str(year)
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            if w[i] == w[j]:
                count += 1
    if count >= 3:
        return True


year_first = int(input('Введите начальный год: '))
year_last = int(input('Введите последний год: '))

for i in range(year_first, year_last):
    year = year_first + 1
    if triada(year):
        print(year)
    year_first = year