'''Возведение матрицы в степень 🌶️

программa возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы, затем натуральное число m.'''

def mult_matrix(matrix1, matrix2, n):
    matrix = []
    for i in range(n):
        row = []
        for r in range(n):
            summ = 0
            for j in range(n):
                mult = matrix1[i][j] * matrix2[j][r]
                summ += mult
            row.append(summ)
        matrix.append(row)

    return matrix


n = int(input())
matrix_in = [[int(i) for i in input().split()] for _ in range(n)]

k = int(input())

for i in range(k - 1):
    matrix = mult_matrix(matrix, matrix_in, n)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
