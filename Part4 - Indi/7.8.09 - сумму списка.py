'''

Напишите функцию list_sum_recursive, которая принимает на вход список из целых чисел и возвращает сумму элементов переданного списка.
Не забывайте, что реализовать это нужно при помощи рекурсии.

Ваша задача только написать определение функции list_sum_recursive

Sample Input:

1 2 3

Sample Output:

6

Напишите программу. Тестируется через stdin → stdout
Верно решили 2 658 учащихся
Из всех попыток 51% верных
Прекрасный ответ. '''


def list_sum_recursive(numers: list) -> int:
    '''возвращает сумму элементов списка'''
    if len(numers) == 1:
        return numers[0]
    return numers.pop() + list_sum_recursive(numers)