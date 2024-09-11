'''

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют слова, написанные строго заглавными латинскими буквами.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, о
круженную символами, соответствующими \W

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

Why isn’t my progress in the APP synchrONized with my progress in the WEB version?

Sample Output 1:

APP WEB

Sample Input 2:

OOO 'BEEGEEK'

Sample Output 2:

OOO BEEGEEK

Sample Input 3:

I will go to the shop aNd you stay At home

Sample Output 3:

I


Верно решили 989 учащихся
Из всех попыток 75% верных
Всё правильно. '''

#regex = r''
regex = r'\b[A-Z]+\b'