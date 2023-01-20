'''
Больше предыдущего
подсчета количества чисел, которые больше предшествующего им в этом списке
'''

count = 0

s = input().split()
for i in range(len(s) - 1):
    if int(s[i + 1]) > int(s[i]):
        count += 1


print(count)
