'''Сложение матриц

программ вычисления суммы двух матриц.'''


n, m = [int(i) for i in input().split()]

matrix1 = [[int(i) for i in input().split()] for _ in range(n)]

input() # пустая строка между строками

matrix2 = [[int(i) for i in input().split()] for _ in range(n)]

matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(m)] for i in range(n)]


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()