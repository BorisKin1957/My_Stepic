'''

Вам доступно регулярное выражение regex, которому соответствуют строки car, cat и cab.
Перепишите его с использованием набора символов, чтобы ему соответствовали те же строки.

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

car cat cab

Sample Output 1:

car cat cab

Sample Input 2:

Car cAt caB caaaaaat carrrrrr-kar

Sample Output 2:

car

Sample Input 3:

Cart carcat caBriolet Cabriolet cabriolet

Sample Output 3:

car cat cab


Верно решили 836 учащихся
Из всех попыток 82% верных
Хорошие новости, верно! '''

#regex = r'car|cat|cab'
regex = r'ca[rbt]'
