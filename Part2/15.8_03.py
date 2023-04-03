'''Напишите функцию is_non_negative_num, используя синтаксис анонимных функций,
которая принимает строковый аргумент и возвращает значение True,
если переданный аргумент является неотрицательным числом (целым или вещественным)
и False в противном случае.

Примечание 1. Следующий программный код:

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))

должен выводить:

False
True
False
False
True
False
False
True

Примечание 2. Неотрицательные числа — это положительные числа и число нуль.'''

is_non_negative_num = lambda s: s[0] != '-' and s.count('.') <= 1 and not sorted(s)[-1].isalpha()

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))
