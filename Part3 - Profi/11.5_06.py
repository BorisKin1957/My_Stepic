'''

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют последовательности символов, представляющие собой девятисимвольные палиндромы.

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

What is palindrome? Examples: -._.-._.-, rotavator, abba, deleveled, 123454321

Sample Output 1:

-._.-._.- rotavator deleveled 123454321

Sample Input 2:

a1.-B-.1a

Sample Output 2:

a1.-B-.1a

Sample Input 3:

atri_c_irtjfien

Sample Output 3:

tri_c_irt


Верно решили 963 учащихся
Из всех попыток 62% верных
Отлично! '''

regex = r'(.)(.)(.)(.).\4\3\2\1'