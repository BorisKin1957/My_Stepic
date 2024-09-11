'''
Итератор Alphabet 🌶️

Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

    language — код языка: ru — русский, en — английский

Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

    русского алфавита, если language имеет значение ru
    английского алфавита, если language имеет значение en

Примечание 1. Буква ё в русском алфавите не учитывается.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

Sample Output 1:

а
б
в

Sample Input 2:

en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

Sample Output 2:

a b c d e f g h i j k l m n o p q r s t u v w x y z a b

'''


class Alphabet:

    def __init__(self, lng):
        self.en = [chr(i) for i in range(97, 123)]
        self.ru = [chr(i) for i in range(1072, 1104)]
        self.lng = lng
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.lng == 'en':
            if self.i < 25:
                self.i += 1
            else:
                self.i -= 25
            return self.en[self.i]
        if self.lng == 'ru':
            if self.i < 31:
                self.i += 1
            else:
                self.i -= 31
            return self.ru[self.i]




ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

print('test 2')

en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

print('test 3')

# en_alpha = Alphabet('en')
#
# for _ in range(100):
#     print(next(en_alpha))

print('test 4')

en_alpha = Alphabet('en')

for _ in range(1000):
    next(en_alpha)

print(next(en_alpha))

print('test 5')

ru_alpha = Alphabet('ru')

for _ in range(1000):
    next(ru_alpha)

print(next(ru_alpha))

print('test 6')
ru_alpha = Alphabet('ru')

for _ in range(50):
    print(next(ru_alpha))

print('test 7')

ru_alpha = Alphabet('ru')

for _ in range(40):
    next(ru_alpha)

for _ in range(40):
    next(ru_alpha)

for _ in range(40):
    next(ru_alpha)

print(next(ru_alpha))

print('test 8')

en_alpha = Alphabet('en')

for _ in range(40):
    next(en_alpha)

for _ in range(40):
    next(en_alpha)

for _ in range(40):
    next(en_alpha)

print(next(en_alpha))


