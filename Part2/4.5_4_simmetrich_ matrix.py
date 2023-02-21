'''Симметричная матрица

программa проверяет симметричность квадратной матрицы
относительно главной диагонали.'''

n = int(input())
flag = True
matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')