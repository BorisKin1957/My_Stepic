'''Транспонирование матрицы.

Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.'''


n = int(input())

matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()


