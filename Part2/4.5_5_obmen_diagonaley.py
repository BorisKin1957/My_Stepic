'''Обмен диагоналей

программa меняет местами элементы, стоящие на главной и побочной диагонали'''

n = int(input())

matrix = [input().split() for _ in range(n)]

for i in range(n):
   matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]

for row in matrix:
    print(*row)
