'''
BEEGEEK

BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.

Напишите функцию is_valid_password(password), которая принимает в качестве
аргумента строковое значение пароля password и возвращает значение True
если пароль является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False

Sample Input:
15551:7:290

Sample Output:
True

'''


# объявление функций
def is_prime(num):
    a = True
    if num == 1:
        a = False
    for i in range(2, num):
        if num % i == 0:
            a = False
            break
    return a


def is_palindrome(text):
    s1 = text.replace(' ', '')
    s = s1.replace(',', '')
    s1 = s.replace('.', '')
    s = s1.replace('-', '')
    s1 = s.replace('!', '')
    s = s1.replace('?', '')

    j = - 1
    flag = True

    for i in range(len(s)):
        if s.lower()[i] != s.lower()[j]:
            flag = False
            break
        j -= 1

    return flag


def is_evan(num1):
    return num1 % 2 == 0


def is_valid_password(password):
    s = password.split(':')
    if len(s) == 3:
        text = s[0]
        num = int(s[1])
        num1 = int(s[2])

        return is_palindrome(text) and is_prime(num) and is_evan(num1)
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
