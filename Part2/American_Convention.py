'''Standard American Convention
вставляет в заданное число запятые в соответствии со стандартным
американским соглашением о запятых в больших числах.'''

s, a = [], '00'
n = int(input())

while n > 999:
    a += str(n % 1000)
    s.append(a[-3:])
    n = n // 1000

s.append(str(n))
s.reverse()

print(','.join(s))
