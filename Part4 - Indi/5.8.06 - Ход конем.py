matrix = [list(input()) for _ in range(8)]

'''Вычислим координаты точки H'''
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'H':
            a, b = i, j
matrix[a][b] = '+'

if a >= 2:
    if b >= 1:
        matrix[a - 2][b - 1] = '+'
    if b <= 6:
        matrix[a - 2][b + 1] = '+'
if a <= 5:
    if b >= 1:
        matrix[a + 2][b - 1] = '+'
    if b <= 6:
         matrix[a + 2][b + 1] = '+'
if b >= 2:
    if a >= 1:
        matrix[a - 1][b - 2] = '+'
    if a <= 6:
        matrix[a + 1][b - 2] = '+'

if b <= 5:
    if a >= 1:
        matrix[a - 1][b + 2] = '+'
    if a <= 6:
        matrix[a + 1][b + 2] = '+'

matrix[a][b] = 'H'

for elem in matrix:
    print(''.join(elem))