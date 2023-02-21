'''Различные элементы
для подсчета количества разных элементов в списке.'''

s = input().split()
count = 1

for i in range(len(s) - 1):
    if s[i + 1] != s[i]:
        count += 1

print(count)