'''Заполнение змейкой

На вход программе подаются два натуральных числа n и m.
программa создает матрицу размером n×mn×m заполнив её "змейкой" в соответствии с образцом:

1  2  3  4  5
10 9  8  7  6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25'''

n, m = [int(i) for i in input().split()]
k = 1
matrix = []
matrix2 = []

for i in range(n):
    row = []
    for j in range(1, m + 1):
      row.append(k)
      k += 1
    matrix.append(row)
matrix2.append(matrix[0])

for j in range(1, n):
    if j % 2 != 0:
        s = matrix[j][::-1]
    else:
        s = matrix[j]
    matrix2.append(s)

for row in matrix2:
    for col in row:
        print(str(col).ljust(3), end=' ')
    print()