'''След матрицы

Следом квадратной матрицы называется сумма элементов главной диагонали.
выводит след заданной квадратной матрицы.'''

n = int(input())
sum = 0
s = []
for i in range(n):
    s.append(input().split())
for i in range(n):
    sum += int(s[i][i])

print(sum)