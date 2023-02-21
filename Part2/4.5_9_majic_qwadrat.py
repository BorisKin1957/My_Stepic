'''Магический квадрат 🌶️

Магическим квадратом порядка n называется квадратная таблица размера n×n,
составленная из всех чисел 1,2,3,…,n21,2,3,…,n2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равны между собой.
программa проверяет, является ли заданная квадратная матрица магическим квадратом.'''

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

flag = True
list = []

for row in matrix:
    for elem in row:
        list.append(elem)
list.sort()

for i in range(len(list)):
    if list[i] in list[i + 1:] or list[i] == 0:
        flag = False
        break

summ, summ2, count = 0, 0, 0
matrix2 = []

for i in range(n):
    summ += matrix[i][i]
    list = []
    for j in range(n):
        list.append(matrix[j][i])
    matrix2.append(list)

for i in range(n):
    summ2 += matrix[n - 1 - i][i]

if summ2 != summ:
    flag = False

for row in matrix:
    if sum(row) != summ:
        flag = False
        break

for row in matrix2:
    if sum(row) != summ:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')