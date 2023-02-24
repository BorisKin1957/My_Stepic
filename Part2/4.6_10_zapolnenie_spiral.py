'''Заполнение спиралью 😈😈

На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×mn×m заполнив её "спиралью" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение


Sample Input 1:

4 5

Sample Output 1:

1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8'''

n, m = [int(i) for i in input().split()]
k, p = 0, 0
s = [['*' for i in range(1, m + 1)] for _ in range(n)]
flag = True

while flag:
    for j in range(p, m - p):
        if k < n * m:
            k += 1
            s[p][j] = k
        else:
            flag = False
            break

    for i in range(p + 1, n - p):
        if k < n * m:
            k += 1
            s[i][m - 1 - p] = k
        else:
            flag = False
            break

    for j in range(p + 1, m - p):
        if k < n * m:
            k += 1
            s[n - 1 - p][-j - 1] = k
        else:
            flag = False
            break

    for i in range(p + 1, n - 1 - p):
        if k < n * m:
            k += 1
            s[n - i - 1][- m + p] = k
        else:
            flag = False
            break
    if k < n * m:
        p += 1
    else:
        flag = False
        break


for row in s:
    for col in row:
        print(str(col).ljust(3), end=' ')
    print()