'''

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют слова, начинающиеся с латинской заглавной буквы.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w,
окруженную символами, соответствующими \W

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

I signed up in the app using my Apple ID. How can I sign in to the web version?

Sample Output 1:

I Apple ID How I

Sample Input 2:

I can Do it MYSELF

Sample Output 2:

I Do MYSELF

Sample Input 3:

How are --U--

Sample Output 3:

How U


Верно решили 975 учащихся
Из всех попыток 48% верных
Здорово, всё верно. '''

#regex = r''
regex = r'\b[A-Z]\w+\b|\b[A-Z]\b'

'''ВЕРНЕЕ

regex = r'\b[A-Z]\w*\b'

regex = r'\b[A-Z]\w{0,}\b'

'''
