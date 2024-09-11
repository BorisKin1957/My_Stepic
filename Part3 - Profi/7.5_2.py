'''
Функция is_good_password() 🐍

Назовем пароль хорошим, если

    его длина равна 9 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:

    LengthError, если его длина меньше 99 символов
    LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
    DigitError, если в нем нет ни одной цифры

Примечание 1. Исключения LengthError, LetterError и DigitError уже определены и доступны.

Примечание 2. Приоритет возбуждения исключений в случае невыполнения нескольких условий: LengthError,
затем LetterError, а уже после DigitError.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_good_password(),
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))

Sample Output 1:

<class '__main__.LengthError'>

Sample Input 2:

print(is_good_password('еПQSНгиfУЙ70qE'))

Sample Output 2:

True

Sample Input 3:

try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))

Sample Output 3:

<class '__main__.LetterError'>


РЕШЕНО В ДРУГОМ чем нужно СТИЛЕ (((

'''

def is_good_password(txt):
    a = True
    for i in txt:
        if i.isalpha():
            a = False
            break
    if len(txt) < 9:
        raise LengthError('no long')
    elif txt.islower() or txt.isupper() or txt.isdigit() or a:
        raise LetterError('bad chars')
    elif txt.isalpha():
        raise DigitError('no digit')
    return True

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

try:
    print(is_good_password('!@#$%^&*()_+'))
except Exception as err:
    print(type(err))