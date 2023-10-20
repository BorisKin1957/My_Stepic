'''
Итератор PowerOf

Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:

    number — ненулевое число

Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных
степеней числа number в порядке возрастания, начиная с нулевой степени.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс PowerOf.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input:

power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))

Sample Output:

1
2
4
8

Верно решили 960 учащихся
Из всех попыток 86% верных
Абсолютно точно. '''


class PowerOf:
    def __init__(self, number):
        self.n = number
        self.pow = -1       # -1 исходное значение степени
    def __iter__(self):
        return self

    def __next__(self):
        self.pow += 1
        return self.n ** self.pow


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))

print('test 2')

power_of_two = PowerOf(1)

for _ in range(55):
    print(next(power_of_two))

print('test 3')

power_of_two = PowerOf(3)

for _ in range(10):
    print(next(power_of_two))

print('test 4')

power_of_two = PowerOf(11)

for _ in range(11):
    print(next(power_of_two))

print('test 5')

power_of_two = PowerOf(100)

for _ in range(20):
    next(power_of_two)

print(next(power_of_two))