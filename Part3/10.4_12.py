'''
Итератор Xrange 🌶️

Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

    start — целое или вещественное число
    end — целое или вещественное число
    step — целое или вещественное число, по умолчанию имеет значение 11

Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end,
включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Xrange.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

evens = Xrange(0, 10, 2)

print(*evens)

Sample Output 1:

0 2 4 6 8

Sample Input 2:

xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')

Sample Output 2:

0.0; 0.5; 1.0; 1.5; 2.0; 2.5

Sample Input 3:

xrange = Xrange(10, 1, -1)

print(*xrange)

Sample Output 3:

10 9 8 7 6 5 4 3 2

Sample Input 4:

xrange = Xrange(5, 10)

print(*xrange)

Sample Output 4:

5 6 7 8 9


Верно решили 874 учащихся
Из всех попыток 35% верных
Здорово, всё верно. '''

class Xrange:
    def __init__(self, start, end, step=1):
        if start < end:
            flag = True
        else:
            flag = False
        L = []
        value = start - step
        if flag:
            while value < end - step:
                value += step
                L.append(value)
        else:
            while value > end - step:
                value += step
                L.append(value)
        self.result = iter(L)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.result)


evens = Xrange(0, 10, 2)

print(*evens)

print('test 2')

xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')

print('test 3')

xrange = Xrange(10, 1, -1)

print(*xrange)
#
# print('test 4')
#
# xrange = Xrange(5, 10)
#
# print(*xrange)
#
# print('test 5')
#
# xrange = Xrange(-20, 12, 4)
#
# print(*xrange)
#
# print('test 6')
#
# xrange = Xrange(-50, -10, 5)
#
# print(*xrange)
#
# print('test 7')
#
# xrange = Xrange(-50, -49)
#
# print(*xrange)
#
# print('test 8')
#
# xrange = Xrange(-50, -48, 2)
#
# print(*xrange)

xrange = Xrange(100.1, 13.7, -3.8)

print(*xrange)
