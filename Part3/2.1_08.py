'''Функция index_of_nearest()

Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:

    numbers — список целых чисел
    number — целое число

Функция должна находить в списке numbers ближайшее по значению число к числу number
и возвращать его индекс. Если список numbers пуст, функция должна вернуть число −1−1.

Примечание 1. Если в функцию передается список, содержащий несколько чисел,
одновременно являющихся ближайшими к искомому числу, функция должна возвращать
наименьший из индексов ближайших чисел.

Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3,
имеющие индексы 1 и 2 соответственно. Наименьший из индексов равен 1.

Sample Input 1:
print(index_of_nearest([], 17))

Sample Output 1:
-1

Sample Input 2:
print(index_of_nearest([7, 13, 3, 5, 18], 0))

Sample Output 2:
2

Sample Input 3:
print(index_of_nearest([9, 5, 3, 2, 11], 4))

Sample Output 3:
1

'''

def index_of_nearest(numbers, num):
    if numbers:
        numbers.append(num)
        new = sorted(numbers[:])            # добавляем в список наше число и сортируем
        before = new[new.index(num) - 1]    # узнаем числа меньшее и большее нашего
        after = new[new.index(num) + 1]
        if abs(abs(num) - abs(before)) < abs(abs(after) - abs(num)): # вычисляем разность, по меньшей разности находим нужное нам число
            return numbers.index(before)
        if abs(abs(num) - abs(before)) == abs(abs(after) - abs(num)): # если разности равны, ищем меньше из 2-ч чисел
            return min([numbers.index(before), numbers.index(after)])

        return numbers.index(after)
    return -1

print(index_of_nearest([1, 1, 1, 1, 1], 1))

'''
А ВОТ КАК УМНЫЕ РЕШАЮТ:

def index_of_nearest(nums, n):
    if nums:
        minimum = min(nums, key=lambda num: abs(num - n))
        return nums.index(minimum)
    return -1


'''