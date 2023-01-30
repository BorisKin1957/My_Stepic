'''Максимальный в области 1
выводит максимальный элемент в
области левее гл диагонали квадратной матрицы'''

n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

s = []
for i in  range(n):
    for j in range(n):
        if i >= j:
            s.append(matrix[i][j])

print(max(s))