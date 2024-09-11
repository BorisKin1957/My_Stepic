'''
Функция range_sum()

Реализуйте функцию range_sum() с использованием рекурсии, которая принимает три аргумента в следующем порядке:

    numbers — список целых чисел
    start — целое неотрицательное число
    end — целое неотрицательное число

Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end]
включительно и возвращать полученный результат.

Примечание 1. Рассмотрим первый тест. Диапазону индексов [3;7] в переданном списке принадлежат
числа4,5,6,7,8сумма которых равна:
4+5+6+7+8=30
4+5+6+7+8=30
Примечание 2. Гарантируется, что start <= end.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию range_sum(),
но не код, вызывающий ее.


Sample Input 1:

print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))

Sample Output 1:

30

Sample Input 2:

print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))

Sample Output 2:

45

Sample Input 3:

print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))

Sample Output 3:

1

'''


def range_sum(numbers, start, end, result=0):
    if start > end:
        return result
    return range_sum(numbers, start + 1, end, result + numbers[start])


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))