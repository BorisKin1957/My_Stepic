'''Произведение чисел
является ли последне число произведением двух чисел из данного набора,
'''

s = []
for i in range(int(input())):
    s.append(input())

multipl = int(input())
flag = False

for i in s:
    if i != '0':
        if str(int(multipl / int(i))) in s[(s.index(i) + 1):]:
            flag = True
            break
if flag:
    print('ДА')
else:
    print('НЕТ')