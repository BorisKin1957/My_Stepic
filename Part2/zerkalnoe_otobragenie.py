'''Зеркальное отображение

программa зеркально отображает элементы матрицы
относительно горизонтальной оси симметрии.'''

n = int(input())

matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n // 2):
        matrix[j][i], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[j][i]

for row in matrix:
    print(*row)