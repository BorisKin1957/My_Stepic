'''Орел и решка
подсчитывает наибольшее количество подряд выпавших Решек.'''

s, count, count_max = input(), 0, 0
for i in s:
    if i == 'Р':
        count += 1
    else:
        if count > count_max:
            count_max = count
        count = 0
if count > count_max:
    print(count)
else:
    print(count_max)