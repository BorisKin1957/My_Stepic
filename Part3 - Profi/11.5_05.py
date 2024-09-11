'''

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют строки, содержащие три или более последовательных повторений ok.

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

Ok, Jim. I said okok! okokokok!

Sample Output 1:

okokokok

Sample Input 2:

OkoKokokOk OKOKOKOKK okokok

Sample Output 2:

okokok

Sample Input 3:

okokokoko okokokokkkkkk

Sample Output 3:

okokokok okokokok

Верно решили 969 учащихся
Из всех попыток 64% верных
Правильно. '''

regex = r'(ok){3,}'