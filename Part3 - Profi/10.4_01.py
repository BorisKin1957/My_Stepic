'''
Итератор Repeater

Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:

    obj — произвольный объект

Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Repeater.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

bee = Repeater('bee')

print(next(bee))

Sample Output 1:

bee

Sample Input 2:

geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))

Sample Output 2:

geek
geek
geek

Из всех попыток 91% верных
Абсолютно точно. '''

class Repeater:
    def __init__(self, obj):  # конструктор принимает аргумент obj (помимо self)
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


bee = Repeater('bee')

print(next(bee))

print('test 2')

geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))

print('test 3')

repeater = Repeater(1234)

for _ in range(100):
    print(next(repeater))

print('test 4')

repeater = Repeater((1, 2, 3, 4))

for _ in range(55):
    print(next(repeater))