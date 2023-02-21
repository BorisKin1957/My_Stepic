'''Максимум в таблице

На вход программе подаются два натуральных числа n и m —
количество строк и столбцов в матрице, затем n строк по m целых чисел
в каждой, отделенных символом пробела.

программa находит индексы (строку и столбец) первого вхождения максимального элемента.'''

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
max, result = matrix[0][0], [0, 0]
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
            result = [i, j]

print(*result)