'''Решение нашел, только тогда когда дошло, что список следует строить, находя суммы в списке от 1 до n
В отличие от решения со словарем, в этом можно посмотреть на сам список из чисел.

Не могу сказать, что это эффективное решение, но в нём, в отличие от решения словарём,
можно поглазеть на итоговый список групп.

Решение станет эффективным, если в коде строку: for i in range(n)
заменить на строку: for i in range(sum_digit(n))'''

def sum_digit(num):
    return sum([int(i) for i in list(str(num))])

n = int(input())
num_list, result = [i for i in range(1, n + 1)], []

for i in range(n):
    l = []
    for num in num_list:
        x = sum_digit(num)
        if x == i:
            l.append(num)
    if l:
        result.append(l)

print(max([len(i) for i in result]))

print(result)