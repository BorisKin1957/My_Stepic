'''Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют строки длины 4545, удовлетворяющие следующим условиям:

    первые 4040 символов являются либо латинскими буквами произвольного регистра, либо четными цифрами
    последние 55 символов являются либо нечетными цифрами, либо символами пробела

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

BpOBNpqKg4EgPKxWn8wavcQMOP06nbCwvOdu6CPj11111

Sample Output 1:

BpOBNpqKg4EgPKxWn8wavcQMOP06nbCwvOdu6CPj11111

Sample Input 2:

BTJubHCvbwTQEN2BqQJsgAIDW4bcyFyUp4COdUO4 3791

Sample Output 2:

BTJubHCvbwTQEN2BqQJsgAIDW4bcyFyUp4COdUO4 3791

Sample Input 3:

Sufk6dm7ECNGRlJ7VsIB7HvBOvSgAoN9gIUOqwy4

Sample Output 3:


Верно решил 971 учащийся
Из всех попыток 69% верных
Прекрасный ответ. '''

#regex = r''
regex = r'^[A-z02468]{40}[013579|\s]{5}$'