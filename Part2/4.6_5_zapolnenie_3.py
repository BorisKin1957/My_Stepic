'''Заполнение 3

На вход программе подается натуральное число n.
программa создает матрицу размером n×n
заполнив её в соответствии с образцом:
разместить единицы на главной и побочной диагоналях,
остальные позиции матрицы заполнить нулями'''

n = int(input())

matrix = [[_ for _ in range(n)] for _ in range(n)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if n - 1 - i == j or i == j:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()