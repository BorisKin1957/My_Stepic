'''Упаковка дубликатов
упаковывает последовательности одинаковых символов заданной строки в подсписки.'''

# l = input().split()
# l_n = [l[0]]
# list = []
# l_ = []

# for i in range(len(l) - 1):
#     if l[i + 1] == l[i]:
#         l_n.append(l[i + 1])
#     else:
#         if i + 2 < len(l) and l[i + 2] != l[i + 1]:
#             l_.append(l[i + 1])
#         else:
#             if l_n:
#                 list += [l_n]
#             l_n = [l[i + 1]]
#             continue
#         if l_n:
#             list += [l_n] + [l_]
#         else:
#             list += [l_]
#         l_n = []
#         l_ = []
#
# print(list + [l_n])
list =[]
s = input().split()

for elem in s:
    if list and elem in list[-1]: # не понял условия if list
        list[-1].append(elem)
    else:
        list.append([elem])

print(list)