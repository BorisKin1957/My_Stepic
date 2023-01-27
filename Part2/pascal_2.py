'''Треугольник Паскаля 2
выводит первые n строк треугольника Паскаля.'''

def pascal(row):
    from math import factorial
    list = []
    for i in range(row + 1):
        list.append(int(factorial(row) / (factorial(i) * factorial(row - i))))
    return(list)

for i in range(int(input())):
    list = []
    list.append(pascal(i))
    print(*list[0])