'''Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter,
где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и
возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:
AB23_56VG          # правильный
V3F_231GT          # неправильный

Примечание 2. Обратите внимание на символ _ в почтовом индексе.
Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.'''

def generate_index():
    import string, random
    s = [_ for _ in string.ascii_uppercase]
    l = []
    l.extend(random.sample(s, 2))
    l.extend(str(random.randint(0, 99)))
    l.extend('_')
    l.extend(str(random.randint(0, 99)))
    l.extend(random.sample(s, 2))


    return ''.join(l)

#print(generate_index())