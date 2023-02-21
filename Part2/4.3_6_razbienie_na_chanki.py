'''Разбиение на чанки
принимает на вход список и число, задающее размер чанка (куска),
а возвращает список из чанков указанной длины.
'''

def chunked(s, k):
    from math import ceil
    list = []
    m = ceil(len(s) / k)
    for i in range(m):
        li = []
        for j in range(k):
            if len(s) >= 1:
                li.append(s.pop(0))
        list.append(li)

    return list

print(chunked(input().split(), int(input())))