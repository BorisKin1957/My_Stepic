'''Алгоритм не оптимален
Потому что основан на сортировке чисел, когда надо было сортировать строки
Выравнивать числа по длине и сортировать лексиграфически'''


def fun(num, lenght):
    bits = len(num)
    if bits == 1:
        result = int(num * lenght)
    else:
        if lenght > 4:
            if bits < lenght:
                k = lenght - bits
                if num[0] < num[1]:
                    result = int((num * k)[:lenght]) + 1
                else:
                    result = int((num * k)[:lenght])
            else:
                result = int(num)
        elif bits < lenght:
            if num[0] < num[1]:
                result = int((num * 2)[:lenght]) + 1
            else:
                result = int((num * 2)[:lenght])
        if bits == lenght:
            result = int(num)

    return result


def get_biggest(numbers):
    if numbers:
        numbers = sorted(numbers, reverse=True)
        new = sorted(numbers, key=lambda num: fun(str(num), len(str(numbers[0]))), reverse=True)
        return int(''.join([str(i) for i in new]))
    return - 1


print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))

''' ВОТ КАК НАДО БЫЛО:

def get_biggest(numbers):
    if numbers:
        numbers = [str(i) for i in numbers]
        bits = len(max(numbers))
        new = sorted(numbers, key=lambda num: num * bits, reverse=True)
        return int(''.join([str(i) for i in new]))
    return - 1'''
