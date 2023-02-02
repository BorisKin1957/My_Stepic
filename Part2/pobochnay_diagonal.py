'''Побочная диагональ

На вход программе подается натуральное число n.
программa создает матрицу размером n×n и заполняет её по следующему правилу:

    числа на побочной диагонали равны 1;
    числа, стоящие выше этой диагонали, равны 0;
    числа, стоящие ниже этой диагонали, равны 2.
'''

n = int(input())

matrix = [[_ for _ in range(n)] for _ in range(n)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if n - 1 - i == j:
            matrix[i][j] = 1
        elif n - 1 - i < j:
            matrix[i][j] = 2
        else:
            matrix[i][j] = 0
for row in matrix:
    for col in row:
        print(col, end=' ')
    print()