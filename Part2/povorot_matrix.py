'''Поворот матрицы

программa поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.'''

n = int(input())

matrix = [input().split() for _ in range(n)]

for i in range(n):
    new = []
    for j in range(n):
        new.append(int(matrix[n - 1 - j][i]))

    print(*new)