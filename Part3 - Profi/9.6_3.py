'''
Функция cyclic_shift()

Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:

    numbers — список целых или вещественных чисел
    step — целое число

Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов,
и возвращать значение None. Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. Т
акже используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию cyclic_shift(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)

Sample Output 1:

[5, 1, 2, 3, 4]

Sample Input 2:

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)

Sample Output 2:

[3, 4, 5, 1, 2]

Хорошие новости, верно! '''


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step > 0:
        for i in range(step):
            numbers[:] = numbers[-1:] + numbers[:-1]
    else:
        for i in range(abs(step)):
            numbers[:] = numbers[1:] + numbers[0:1]


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers)

numbers = [1, 2.0, 3, 4.0, 5.5]
cyclic_shift(numbers, 0)
print(numbers)

annotations = cyclic_shift.__annotations__
print(annotations['return'])
print(annotations['step'])

print(*cyclic_shift.__annotations__.values())