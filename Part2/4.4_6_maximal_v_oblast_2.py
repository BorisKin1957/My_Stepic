'''Максимальный в области 2
максимальный элемент в заштрихованной области квадратной матрицы
2 диагонали  между ними, слева и права'''

n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

s = []
for i in  range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            s.append(matrix[i][j])

print(max(s))