'''Алгоритм не оптимален
Потому что основан на сортировке чисел, когда надо было сортировать строки
Выравнивать числа по длине и сортировать лексиграфически



Функция get_biggest() 🌶️🌶️

Реализуйте функцию get_biggest(), которая принимает один аргумент:

    numbers — список целых неотрицательных чисел

Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
Если список numbers пуст, функция должна вернуть число −1−1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
123,132,213,231,312,321
123,132,213,231,312,321 Наибольшим из представленных является 321321.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_biggest(),
но не код, вызывающий ее.



Sample Input 1:
print(get_biggest([1, 2, 3]))

Sample Output 1:
321

Sample Input 2:
print(get_biggest([61, 228, 9, 3, 11]))

Sample Output 2:
961322811

Sample Input 3:
print(get_biggest([7, 71, 72]))

Sample Output 3:
77271

Sample Input 4:
print(get_biggest([]))

Sample Output 4:
-1

'''


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
