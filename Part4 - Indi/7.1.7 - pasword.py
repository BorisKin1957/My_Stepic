'''Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

Сложным паролем будет считаться комбинация символов, в которой :

    Есть хотя бы 3 цифры
    Есть хотя бы одна заглавная буква
    Есть хотя бы один символ из следующего набора "!@#$%*"
    Общая длина не менее 10 символов

Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"

Вам необходимо написать только определение функции check_password'''

def check_password(stroke):
    flag, count_d, count_s, count_i = False, 0, 0, 0
    for char in stroke:
        if char.isdigit():
            count_d += 1
        elif char.isupper():
            count_s += 1
        elif char in '!@#$%*':
            count_i += 1

    if count_i >= 1 and count_s >= 1 and len(stroke) >= 10 and count_d >= 3:
        flag = True
    print('Perfect password' if flag else 'Easy peasy')