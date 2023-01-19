'''Переворот числа
изменит порядок его последних пяти цифр на обратный'''

s = []
s.extend(input())
if len(s) > 5:
    s1 = s[1:]
    s1.reverse()
    print(s[0], *s1, sep='')
else:
    s.reverse()
    s = int(''.join(s))
    print(s)