'''Подсписки списка
выводит список, содержащий все возможные подсписки списка, включая пустой список.'''

s = input().split()
sp = []
k = len(s)
sp.append([])
for i in range(k):
    sp.append([s[i]])
for j in range(2, k + 1):
    for i in range(k):
        sp.append(s[i:i + j])
    sp = sp[:-(j - 1)]

print(sp)