'''Симметричная матрица

программa проверки симметричности квадратной матрицы относительно побочной диагонали.'''

n = int(input())
flag = True

matrix = [input().split() for _ in range(n)]

matrix.reverse()

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')