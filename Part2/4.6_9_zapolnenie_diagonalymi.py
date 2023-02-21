'''Заполнение диагоналями 🌶️

На вход программе подаются два натуральных числа n и m.
программуa создает матрицу размером n×m заполнив её "диагоналями" в соответствии с образцом:

1  2  4  7
3  5  8  10
6  9  11 12'''

n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]
k = 0

for q in range(n + m + 1):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                k += 1
                matrix[i][j] = k

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()