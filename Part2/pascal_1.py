'''Треугольник Паскаля 1
 возвращает указанную строку треугольника Паскаля в виде списка
 (нумерация строк начинается с нуля).'''

def pascal(row):
    from math import factorial
    list = []
    for i in range(row + 1):
        list.append(int(factorial(row) / (factorial(i) * factorial(row - i))))
    return(list)

print(pascal(int(input())))