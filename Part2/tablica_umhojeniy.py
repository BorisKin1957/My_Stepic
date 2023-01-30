'''Таблица умножения

На вход программе подаются два натуральных числа n и m —
количество строк и столбцов в матрице. Создайте матрицу mult размером n×m
и заполните её таблицей умножения по формуле mult[i][j] = i * j.'''

n, m = int(input()), int(input())

for i in range(n):
    row = [str(i * j) for j in range(m)]
    for k in range(len(row)):
        print(row[k].ljust(3), end='')
    print()