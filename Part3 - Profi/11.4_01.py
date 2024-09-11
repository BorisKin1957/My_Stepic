'''

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют слова a, A, an и An.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w,
окруженную символами, соответствующими \W

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

A cow is an animal.

Sample Output 1:

A an

Sample Input 2:

I have been reading this text for aN hour. Сan you give me this book? AN or an apple

Sample Output 2:

an

Sample Input 3:

An acle, a Ancle, A antarktida, an Any

Sample Output 3:

An a A an

Верно решил 961 учащийся
Из всех попыток 64% верных
Прекрасный ответ. '''

#regex = r''
regex = r'\b[Aa]\b|\b[Aa]n\b'

'''ТОЧНЕЕ

regex = r'\b[Aa]n?\b
'''