'''
Функция first_largest()

Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект, элементами которого являются целые числа
    number — произвольное число

Функция должна возвращать индекс первого элемента итерируемого объекта iterable,
который больше number. Если таких элементов нет, функция должна вернуть число −1.

Примечание 1. Рассмотрим список чисел 10,2,14,7,7,18,2010,2,14,7,7,18,20 из первого теста.
Первым числом, превосходящим 1111, является число 1414, которое имеет индекс 22.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_largest(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

Sample Output 1:

2

Sample Input 2:

iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))

Sample Output 2:

-1

Sample Input 3:

iterator = iter([18, 21, 14, 72, 73, 18, 20])

print(first_largest(iterator, 10))

Sample Output 3:

0

Верно решили 953 учащихся
Из всех попыток 61% верных
Здорово, всё верно. '''

def first_largest(iterable, n):
    i = 0
    iterator = iter(iterable)
    try:
        while next(iterator) < n:
            i += 1
        return i
    except:
        return -1

numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

print('test 2')

iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))

print('test 3')

iterator = iter([18, 21, 14, 72, 73, 18, 20])

print(first_largest(iterator, 10))

print('test 4')

iterator = iter([18, 21, 14, 72, 73, 18, 20, 101, 102, 110])

print(first_largest(iterator, 105))

print('test 5')

iterator = iter([123, 423, 224, 722, 713, 158, 230, 1101, 1022, 1210, 222, 333, 334])

print(first_largest(iterator, 105))

print('test 6')

iterator = iter([2, 3, 4, 5, 6, 7, 8, 999])

print(first_largest(iterator, 105))

print('test 7')

iterator = iter([999])

print(first_largest(iterator, 105))

print('test 8')

iterator = iter([998])

print(first_largest(iterator, 999))