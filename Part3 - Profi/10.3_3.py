'''
Функция is_iterator()

Реализуйте функцию is_iterator(), которая принимает один аргумент:

    obj — произвольный объект

Функция должна возвращать True, если объект obj является итератором, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_iterator(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(is_iterator([1, 2, 3, 4, 5]))

Sample Output 1:

False

Sample Input 2:

beegeek = map(str.upper, 'beegeek')

print(is_iterator(beegeek))

Sample Output 2:

True

Sample Input 3:

beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))

Sample Output 3:

True


Верно решили 975 учащихся
Из всех попыток 74% верных
Правильно, молодец! '''


def is_iterator(obj):
    try:
        iter(obj)
        if iter(obj) == obj:
            return True
        else:
            return False
    except:
        return False

'''ТОЧНЕЕ:

def is_iterator(obj):
    try:
        next(obj)
        return True
    except TypeError:
        return False

'''


print(is_iterator([1, 2, 3, 4, 5]))

print('2')

beegeek = map(str.upper, 'beegeek')

print(is_iterator(beegeek))

print('3')

beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))

print('7')

beegeek = 199999111199991919191

print(is_iterator(beegeek))

print('8')

beegeek = iter('199999111199991919191')

print(is_iterator(beegeek))