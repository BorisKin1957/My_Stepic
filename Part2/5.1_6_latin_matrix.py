'''Латинский квадрат

Латинским квадратом порядка n называется квадратная матрица размером n×n,
каждая строка и каждый столбец которой содержат все числа от 1 до n.
программa проверяет, является ли заданная квадратная матрица латинским квадратом.'''


def latin(matrix, n):
#    global flag
    flag = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[-(i + 1)][j]:
                flag = False
                break

    return flag


def sort_row(matrix, n):
    for i in range(n):
        matrix[i].sort()

    return matrix


n = int(input())

matrix = [input().split() for _ in range(n)]


matrix1 = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    matrix1.append(row)

sort_row(matrix, n)

flag = latin(matrix, n)

if flag:
    sort_row(matrix1, n)
    flag = latin(matrix1, n)

for i in range(len(matrix[0]) - 1):
    if matrix[0][i + 1] == matrix[0][i]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')