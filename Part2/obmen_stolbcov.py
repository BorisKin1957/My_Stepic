'''Обмен столбцов

программa меняет местами столбцы в матрице.'''

n, m = int(input()), int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

k = [int(i) for i in input().split()]

# for i in range(n):
#     a = matrix[i][k[0]]
#     b = matrix[i][k[1]]
#     matrix[i][k[0]] = b
#    matrix[i][k[1]] = a

for i in range(n):
    matrix[i][k[0]], matrix[i][k[1]] = matrix[i][k[1]], matrix[i][k[0]] # вот верно взамен предыдущего цикла

for row in matrix:
    print(*row)
