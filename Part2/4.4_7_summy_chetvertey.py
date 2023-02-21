'''Суммы четвертей
вычисляет у матрицы сумму элементов:
верхней четверти; правой четверти; нижней четверти; левой четверти.'''

n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

s_up, s_r, s_l, s_d = [], [], [], []

for i in  range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            s_up.append(matrix[i][j])
        elif i < j and i > n - 1 - j:
            s_r.append(matrix[i][j])
        elif i > j and i < n - 1 - j:
            s_l.append(matrix[i][j])
        elif i > j and i > n - 1 - j:
            s_d.append(matrix[i][j])

print('Верхняя четверть:', sum(s_up))
print('Правая четверть:', sum(s_r))
print('Нижняя четверть:', sum(s_d))
print('Левая четверть:', sum(s_l))