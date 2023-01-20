'''Назад, вперёд и наоборот
меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д'''

s = input().split()
s_last = [0]

if len(s) % 2 != 0:
    s_last = s[-1]
    s = s[:-1]

for i in range(1, len(s), 2):
    s_new = s[:2]
    s_new = s_new[::-1]
    s = s[2:]
    s.extend(s_new)

if s_last != [0]:
    s.append(s_last)

print(*s)