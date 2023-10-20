'''
Функция get_min_max() 😳

Реализуйте функцию get_min_max(), которая принимает один аргумент:

    iterable — итерируемый объект, элементы которого сравнимы между собой

Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент
итерируемого объекта iterable, вторым — максимальный элемент итерируемого объекта iterable.
Если итерируемый объект iterable пуст, функция должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

iterable = iter(range(10))

print(get_min_max(iterable))

Sample Output 1:

(0, 9)

Sample Input 2:

iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

Sample Output 2:

(1, 33)

Sample Input 3:

iterable = iter([])

print(get_min_max(iterable))

Sample Output 3:

None


Из всех попыток 22% верных
Абсолютно точно. '''


def get_min_max(iterable):
    try:
        tmp = next(iter(iterable))
        min_item, max_item = tmp, tmp
        for i in iterable:
            if i < min_item:
                min_item = i
            elif i > max_item:
                max_item = i
        return min_item, max_item
    except:
        return None


iterable = iter(range(10))

print(get_min_max(iterable))

print('4')

data = iter((9, 9, 9, 9, 9))

print(get_min_max(data))

print('11')

data = iter(range(100_000_000))

print(get_min_max(data))
