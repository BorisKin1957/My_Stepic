'''
Функция verification()

Реализуйте функцию verification(), которая проверяет правильность введенного пароля.
 Она должна принимать четыре аргумента в следующем порядке:

    login — логин пользователя
    password — пароль пользователя
    success — некоторая функция
    failure — некоторая функция

Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква,
хотя бы одна строчная латинская буква и хотя бы одна цифра. Функция verification() должна вызывать функцию success()
с аргументом login, если переданный пароль является правильным, иначе — функцию failure()
с аргументами login и строкой-сообщением об ошибке:

    в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
    в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
    в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
    в пароле нет ни одной цифры, если в пароле отсутствуют цифры

Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения об ошибке являются следующими:

    в пароле нет ни одной буквы

    в пароле нет ни одной заглавной буквы

    в пароле нет ни одной строчной буквы

    в пароле нет ни одной цифры

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию verification(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)

Sample Output 1:

Привет, timyrik20!

Sample Input 2:

def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)

Sample Output 2:

Ruslan_Chaniev, попробуйте снова. Текст ошибки: в пароле нет ни одной заглавной буквы

Правильно.

'''

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

def verification(login, password, success, failure):
    dig, big, lit = False, False, False
    for char in password:
        if char.isdigit():
            dig = True
        elif 64 < ord(char) < 91:
            big = True
        elif 96 < ord(char) < 123:
            lit = True
    if not big and not lit:
        err = 'в пароле нет ни одной буквы'
    elif not big and lit:
        err = 'в пароле нет ни одной заглавной буквы'
    elif not lit and big:
        err = 'в пароле нет ни одной строчной буквы'
    elif not dig:
        err = 'в пароле нет ни одной цифры'
    else:
        err = ''
    if not err:
        success(login)
    else:
        failure(login, err)


verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)
verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
verification('Arthur_Davletov', 'мойпароль123', success, failure)
verification('Arthur_Davletov', 'Python777', success, failure)
verification('Arthur_Davletov', '797777777777', success, failure)