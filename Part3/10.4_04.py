'''
Итератор Fibonacci

Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 11.

Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел,
где каждое последующее число является суммой двух предыдущих:
1,1,2,3,5,8,13,21,34
1,1,2,3,5,8,13,21,34

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Fibonacci.

Примечание 3. Тестовые данные доступны по ссылкам:

Sample Input 1:

fibonacci = Fibonacci()

print(next(fibonacci))

Sample Output 1:

1

Sample Input 2:

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

Sample Output 2:

1
1
2
3


Верно решили 942 учащихся
Из всех попыток 73% верных
Всё получилось! '''


class Fibonacci:
    def __init__(self):
        self.f = [1, 1]  # объявляю переменную self.f, как список ряда Фибоначчи

    def __iter__(self):
        return self

    def __next__(self):
        self.f.append(self.f[-1] + self.f[-2])
        return self.f[-3]  # возвращаю именно третий с конца списка


'''КОРОТКО и ПРОСТО так:

class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

'''

fibonacci = Fibonacci()

print(next(fibonacci))

print('test 2')

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

print('test 3')

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

print('test 4')

fibonacci = Fibonacci()

for _ in range(50):
    print(next(fibonacci))

print('test 5')

fibonacci = Fibonacci()

for _ in range(100):
    next(fibonacci)

print(next(fibonacci))

print('test 6')

fibonacci = Fibonacci()

for _ in range(76):
    next(fibonacci)

next(fibonacci)
next(fibonacci)
next(fibonacci)
next(fibonacci)

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))