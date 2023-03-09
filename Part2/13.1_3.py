'''Дополните приведенный код, чтобы он вывел сумму
наибольшей и наименьшей цифры Decimal числа.'''

from decimal import *
num = Decimal(input())

l = sorted(list(str(abs(num))))

print(int(l[1]) + int(l[-1]))

'''Не добавляется 0 целых цифра в методе  as_tuple().digit'''