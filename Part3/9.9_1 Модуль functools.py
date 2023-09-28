'''
Две функции

Вам доступна уже реализованная функция send_email(), которая принимает три аргумента в следующем порядке:

    name — имя
    email_address — адрес электронной почты
    text — содержание письма

Функция отправляет письмо пользователю с именем name на адрес email_address с содержанием text.

1. Реализуйте функцию to_Timur() с помощью функции partial(), которая принимает один аргумент:

    text — содержание письма

Функция должна отправлять письмо пользователю с именем Тимур на адрес timyrik20@beegeek.ru с содержанием text.

2. Реализуйте функцию send_an_invitation() с помощью функции partial(), которая принимает два аргумента в следующем порядке:

    name — имя
    email_address — адрес электронной почты

Функция должна отправлять письмо на имя name и на адрес email_address со следующим содержанием:

Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....

Примечание 1. Функции to_Timur() и send_an_invitation() должны являться partial объектами.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимые функции to_Timur()
и send_an_invitation(), но не код, вызывающий их.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Напишите программу. Тестируется через stdin → stdout
Верно решили 909 учащихся
Из всех попыток 24% верных
Верно. Так держать! '''


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'


def to_Timur(text):
    return send_email('Тимур', 'timyrik20@beegeek.ru', text)


def send_an_invitation(name, email_address):
    return to_Timur('Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')



print(to_Timur('Тимур, привет, я на егэ, помоги решить 13 задачу'))

print('4')

try:
    to_Timur()
except:
    print('ok')

print('5')

try:
    to_Timur('первое', 'второе')
except:
    print('ok')


print('7')

try:
    to_Timur('beegeek')
    print('ok')
except:
    print('ne ok')

print('8')

print(send_an_invitation("РўРёРјСѓСЂ", "timyrik20@beegeek.ru"))

'''НАДО было ТАК:

from functools import partial

to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')
send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')

'''