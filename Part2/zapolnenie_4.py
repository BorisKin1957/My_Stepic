'''Заполнение 4

На вход программе подается натуральное число n.
программa создает матрицу размером n×n
заполнив её в соответствии с образцом:
1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 1 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1 1 '''

n = int(input())

matrix = [[_ for _ in range(n)] for _ in range(n)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = 0
        if (i < j and i < n - 1 - j) or (i > j and i > n - 1 - j):
            matrix[i][j] = 1
        elif i == j or i == n - 1 - j:
            matrix[i][j] = 1
for row in matrix:
    for col in row:
        print(str(col).ljust(3), end=' ')
    print()