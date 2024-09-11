'''

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют последовательности формата xxx.xxx, где x — любой символ.

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

Hello.How are you today?

Sample Output 1:

llo.How

Sample Input 2:

I read the letter.Stood up.Sat down.Pondered for a minute.Then reread the letter again.

Sample Output 2:

ter.Sto  up.Sat own.Pon ute.The


Верно решили 973 учащихся
Из всех попыток 83% верных
Хорошие новости, верно! '''

regex = r'.{3}\..{3}'
