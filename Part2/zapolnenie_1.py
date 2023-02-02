'''Заполнение 1

На вход программе подаются два натуральных числа n и m.
программa создает матрицу размером n×m
и заполняет её числами от 1 до n*m в соответствии с образцом'''

n, m = [int(i) for i in input().split()]
k = 0
matrix = []

for _ in range(n):
    list = []
    for _ in range(m):
        k += 1
        list.append(k)
    matrix.append(list)

for row in matrix:
    for col in row:
        print(str(col).ljust(3), end=' ')
    print()