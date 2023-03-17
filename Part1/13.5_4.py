'''Good password 🌶️

Напишите функцию is_password_good(password), которая принимает в качестве аргумента
строковое значение пароля password и возвращает значение True
если пароль является надежным и False в противном случае.

Пароль является надежным если:

    его длина не менее 8 символов;
    он содержит как минимум одну заглавную букву (верхний регистр);
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.

 Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

должен выводить:

True
False

'''


# объявление функции
def is_password_good(password):
    s1 = password
    for i in range(len(password)):
        if password[i].isdigit():
            s1 = s1.replace(password[i], '')
    if 7 < len(password) > len(s1):
        if not s1.islower() and not s1.isupper() and s1 != '':
            return True
        else:
            return False
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
