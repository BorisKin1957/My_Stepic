'''
Змеиный регистр

Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента
строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.
Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

должен выводить:

this_is_camel_cased
is_prime_number

Sample Input:
ThisIsCamelCased

Sample Output:
this_is_camel_cased

'''


# объявление функции
def convert_to_python_case(s):
    new = s[0]
    for i in range(1, len(s)):
        if s[i].isupper():
            new += '_' + s[i]
        else:
            new += s[i]
    return new.lower()


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
