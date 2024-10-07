matrix = [list(input()) for _ in range(8)]

'''Вычислим координаты точки F'''
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'T':
            a, b = i, j
matrix[a][b] = '+'

'''Вертикаль'''

for i in range(8):
    matrix[i][b] = '+'

'''Горизонталь'''

for j in range(8):
    matrix[a][j] = '+'

matrix[a][b] = 'T'

for elem in matrix:
    print(''.join(elem))