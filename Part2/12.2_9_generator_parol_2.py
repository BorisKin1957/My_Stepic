'''Генератор паролей 2 🌶️

Напишите программу, которая с помощью модуля random генерирует
n паролей длиной m символов, состоящих из строчных и прописных
английских букв и цифр, кроме тех, которые легко перепутать между собой:

    «l» (L маленькое);
    «I» (i большое);
    «1» (цифра);
    «o» и «O» (большая и маленькая буквы);
    «0» (цифра).

Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра

и как минимум по одной букве в верхнем и нижнем регистре.

Формат входных данных
На вход программе подаются два числа nn и mm, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести nn паролей длиной mm символов в соответствии с
условием задачи, каждый на отдельной строке.

Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые
пароли сгенерировать возможно.

Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:

    функция generate_password(length) – возвращает случайный пароль длиной l
    ength символов;
    функция generate_passwords(count, length) – возвращает список, с
    остоящий из count случайных паролей длиной length символов.

Sample Input 1:
9
7

Sample Output 1:
iHnPg7q
Njj9m3N
tQ9v5ut
6qPZ3tV
6gVScya
kU8ncAY
5CKX9Da
UTQRve4
FyRe8NN'''

def generate_password(length):
    import string, random
    l = set(string.ascii_letters + string.digits) - set('lI1oO0')
    l_upper = set(string.ascii_uppercase) - set('IO')
    l_lower = set(string.ascii_lowercase) - set('ol')
    l_digit = set(string.digits) - set('10')

    l = list(l)
    l_upper = list(l_upper)
    l_lower = list(l_lower)
    l_digit = list(l_digit)

    password = random.sample(l, length - 3)
    password.append(random.choice(l_digit))
    password.append(random.choice(l_upper))
    password.append(random.choice(l_lower))
    random.shuffle(password)

    return ''.join(password)


def generate_passwords(count, length):
    l = [generate_password(length) for _ in range(count)]

    return l

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')