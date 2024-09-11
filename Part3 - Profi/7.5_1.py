'''
Функция is_good_password() 👀

Назовем пароль хорошим, если

    его длина равна 99 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль,
или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу,
содержащую только необходимую функцию is_good_password(),
но не код, вызывающий ее.

Sample Input 1:

print(is_good_password('41157082'))

Sample Output 1:

False

Sample Input 2:

print(is_good_password('мойпарольсамыйлучший'))

Sample Output 2:

False

Sample Input 3:

print(is_good_password('МойПарольСамыйЛучший111'))

Sample Output 3:

True

'''

def is_good_password(s):
    L = set()
    for i in s:
        if i.islower():
            L.add(1)
        elif i.isupper():
            L.add(2)
        elif i.isalnum():
            L.add(3)
    if sum(L) == 6 and len(s) > 8:
        return True
    else:
        return False


print(is_good_password('МойПарольСамыйЛучший111'))
print(is_good_password('41157082'))
print(is_good_password('!@#$%^&*()_+'))
print(is_good_password('4abcdABC'))
print(is_good_password('abc!@#%$#%#$%^&dABC8'))