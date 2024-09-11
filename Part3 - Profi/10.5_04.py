'''
Функция reverse()

Реализуйте генераторную функцию reverse(), которая принимает один аргумент:

    sequence — последовательность

Функция должна возвращать генератор, порождающий элементы последовательности sequence в обратном порядке,
а затем возбуждающий исключение StopIteration.

Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину.
Например, объекты типа list, str, tuple являются последовательностями.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию reverse(),
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(*reverse([1, 2, 3, 4, 5]))

Sample Output 1:

5 4 3 2 1

Sample Input 2:

generator = reverse('beegeek')

print(type(generator))
print(*generator)

Sample Output 2:

<class 'generator'>
k e e g e e b

Верно решили 966 учащихся
Из всех попыток 91% верных
Правильно. '''


def reverse(data):
    for _ in range(len(data)):
        yield data[-1]
        data = data[:-1]

print(*reverse([1, 2, 3, 4, 5]))

print('test 2')

generator = reverse('beegeek')

print(type(generator))
print(*generator)

print('test 3')

generator = reverse('stepik')

print(type(generator))

try:
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')

print('test 4')

generator = reverse(list(range(123, 5453, 3)))

print(type(generator))
print(*generator)

print('test 5')

generator = reverse(tuple('HFJDHFjdhfjhfdJSHFJDHF'))

print(type(generator))

try:
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')


print('test 6')

generator = reverse(list('HFJDHFjd23423i942313223hfjhfdJSHFJD656754964HF'))

print(type(generator))
print(*generator)

print('test 7')

generator = reverse([1])

print(type(generator))
print(*generator)

print('test 8')

print(list(reverse([])))
