'''
Генератор безопасных паролей

Описание проекта: программа генерирует заданное количество паролей
и включает в себя умную настройку на длину пароля, а также на то,
какие символы требуется в него включить, а какие исключить.

Составляющие проекта:

    Целые числа (тип int);
    Переменные;
    Ввод / вывод данных (функции input() и print());
    Условный оператор (if/elif/else);
    Цикл for;
    Написание пользовательских функций;
    Работа с модулем random для генерации случайных чисел.

'''


def generate_password(chars, length):
    pasword = ''
    pasw_ = random.sample(chars, length)
    for i in pasw_:
        pasword += chr(i)
    return pasword


import random

bad_simb = [ord('i'), ord('l'), ord('1'), ord('L'), ord('o'), ord('0'), ord('O')]
pasw = []

pasw_num = int(input('Задайте количество нужных вам паролей: '))
length = int(input('Задайте количество символов для паролей: '))

if input('Включать ли цифры? [ Y/N ]:').lower() == 'y':
    for i in range(48, 58):
        pasw.append(i)

if input('Включать ли прописные буквы? [ Y/N ]:').lower() == 'y':
    for i in range(65, 91):
        pasw.append(i)

if input('Включать ли строчные буквы? [ Y/N ]:').lower() == 'y':
    for i in range(97, 123):
        pasw.append(i)

if input('Включать ли символы !#$%&*+-=?@^ [ Y/N ]:').lower() == 'y':
    for i in range(33, 48):
        pasw.append(i)

if input('Исключать ли неоднозначные символы il1Lo0O [ Y/N ]:').lower() == 'y':
    for i in range(len(pasw)):
        if pasw[i] in bad_simb:
            s = pasw[i]
            pasw.remove(s)
            pasw.insert(i, s + 2)

chars = random.sample(pasw, len(pasw))

print()

for i in range(1, pasw_num + 1):
    pasword = generate_password(chars, length)
    print('Ваш', i, 'пароль:', pasword)

