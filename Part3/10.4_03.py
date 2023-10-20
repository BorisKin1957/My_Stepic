'''
Итератор Square

Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:

    n — натуральное число,

Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых является
квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.

Примечание 1. Последовательность квадратов натуральных чисел начинается с квадрата числа 11.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Square.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

squares = Square(2)

print(next(squares))
print(next(squares))

Sample Output 1:

1
4

Sample Input 2:

squares = Square(10)

print(list(squares))

Sample Output 2:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Sample Input 3:

squares = Square(1)

print(list(squares))

Sample Output 3:

[1]


Верно решили 963 учащихся
Из всех попыток 81% верных
Всё получилось! '''


class Square:
    def __init__(self, n):
        self.n = n
        self.i = 0         # заявляем переменную i
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return self.i ** 2


squares = Square(2)

print(next(squares))
print(next(squares))

print('test 2')

squares = Square(10)

print(list(squares))

print('test 3')

squares = Square(1)

print(list(squares))

print('test 4')

squares = Square(5)

next(squares)
next(squares)
next(squares)
next(squares)
next(squares)

try:
    next(squares)
except StopIteration:
    print('Error')

print('test 5')

squares = Square(9)

print(*squares)

print('test 6')

squares = Square(2)

try:
    print(next(squares))
    print(next(squares))
    print(next(squares))
except:
    print('Error')