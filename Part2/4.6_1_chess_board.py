'''Шахматная доска

На вход программе подаются два натуральных числа n и m.
Напишите программу для создания матрицы размером n×mn×m,
заполнив её символами . и * в шахматном порядке.
В левом верхнем углу должна стоять точка.
Выведите полученную матрицу на экран, разделяя элементы пробелами.'''

s = input().split()

n = int(s[0])
m = int(s[1])

matrix = [[_ for _ in range(1, m + 1)] for _ in range(n)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i + 1) % 2 == 0:
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = '.'
            else:
                matrix[i][j] = '*'
        else:
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = '*'
            else:
                matrix[i][j] = '.'

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()
