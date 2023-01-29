'''Вывести матрицу 1
 считывает элементы матрицы один за другим, затем выводит их в виде матрицы.'''

n, m = int(input()), int(input())
for i in range(n):
    s = []
    for j in range(m):
        s.append(input())
    print(*s)
