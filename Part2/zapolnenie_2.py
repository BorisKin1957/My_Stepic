'''Заполнение 2

На вход программе подаются два натуральных числа n и m.
программa создает матрицу размером n×m
и заполняет её числами от 1 до n*m в соответствии с образцом
1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21'''

n, m = [int(i) for i in input().split()]
k = 0
matrix = [[_ for _ in range(m)] for _ in range(n)]

for j in range(m):
    for i in range(n):
        k += 1
        matrix[i][j] = k

for row in matrix:
    for col in row:
        print(str(col).ljust(3), end=' ')
    print()