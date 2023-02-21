'''Заполнение 5

На вход программе подаются два натуральных числа n и m.
программa создает матрицу размером n×m заполнив её в соответствии с образцом:

1 2 3 4 5 6
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 4
6 1 2 3 4 5
'''

n, m = [int(i) for i in input().split()]

matrix, row = [], []
for i in range(1, m + 1):
      row.append(i)
matrix.append(row)

for j in range(n - 1):
    s = row[1:]
    s.append(row[0])
    matrix.append(s)
    row = s[:]

for row in matrix:
    for col in row:
        print(str(col).ljust(3), end=' ')
    print()