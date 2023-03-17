'''
Палиндром 🌶️

Напишите функцию is_palindrome(text), которая принимает в качестве аргумента
строку text и возвращает значение True если указанный текст является палиндромом
и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми,
а также игнорируйте пробелы, а также символы , . ! ? -.

Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))

должен выводить:

True
True
False

Тестовые данные 🟢

Sample Input:
Standart - smallest, sell Amstrad nats.

Sample Output:
True

'''


# объявление функции
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


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
