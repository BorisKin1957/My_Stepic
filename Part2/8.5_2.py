s = ''

for i in range(int(input())):
    s += input().lower()
print(len(set(s)))