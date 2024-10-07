matrix = [list(input()) for _ in range(8)]

'''Вычислим координаты точки S'''
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'S':
            a, b = i, j
matrix[a][b] = '+'

'''Диагональ слева вниз'''
for i in range(a, 7):
    for j in range(b, 7):
        matrix[i + 1][j + 1] = matrix[i][j]

for i in range(a, 0, -1):
    for j in range(b, 0, -1):
        matrix[i - 1][j - 1] = matrix[i][j]

'''Диагональ слева вверх'''
for i in range(a, 0, -1):
    for j in range(b, 7):
        matrix[i - 1][j + 1] = matrix[i][j]

for i in range(a, 7):
    for j in range(b, 0, -1):
        matrix[i + 1][j - 1] = matrix[i][j]

matrix[a][b] = 'S'

for elem in matrix:
    print(''.join(elem))