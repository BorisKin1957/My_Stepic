'''Умножение матриц 🌶️

рограммa, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице,
затем элементы первой матрицы, затем пустая строка. Далее следуют числа m и k —
количество строк и столбцов второй матрицы затем элементы второй матрицы.'''

n, m = [int(i) for i in input().split()]

matrix1 = [[int(i) for i in input().split()] for _ in range(n)]

input() # пустая строка между строками

m, k = [int(i) for i in input().split()]

matrix2 = [[int(i) for i in input().split()] for _ in range(k)]

matrix = []

for i in range(n):
    row = []
    for r in range(n):
        summ = 0
        for j in range(m):
            mult = matrix1[i][j] * matrix2[j][r]
            summ += mult
        row.append(summ)
    matrix.append(row)

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()