'''
HTML 🌶️🌶️

HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) и конечным (закрывающим) тегами.
Открывающий и закрывающий теги содержат имя элемента. Открывающий тег может содержать дополнительную информацию —
атрибуты и значения атрибутов:

<b>BeeGeek</b>
<a href="https://stepik.org">Stepik</a>

В примере выше тег <b> не содержит никаких атрибутов, а тег <a> содержит атрибут href со значением https://stepik.org.

Напишите программу, которая находит во фрагменте HTML-страницы все атрибуты каждого тега.

Формат входных данных
На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

Формат выходных данных
Программа должна найти в введенном фрагменте HTML-страницы все теги и вывести их, указав для каждого соответствующие атрибуты.
Теги вместе со всеми атрибутами должны быть расположены каждый на отдельной строке, в следующем формате:

<тег>: <атрибут>, <атрибут>, ...

Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.

Примечание 1. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Примечание 2. Некоторые теги не требуют закрытия. Об этом можно почитать здесь.

Sample Input 1:

<p><a href="https://stepik.org">Stepik</a></p>
<div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>

Sample Output 1:

a: href
div: class
p:

Sample Input 2:

<div id="oldie-warning" class="do-not-print">
    <p>
        <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
        <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
    </p>
</div>

Sample Output 2:

a: href
div: class, id
em:
p:
strong:


Верно решили 760 учащихся
Из всех попыток 29% верных
Так точно! '''

import re, sys

D1 = {}
for line in sys.stdin:
    string = line.split('>')
    for word in string:
        regex = r'<([\w+-]+)| ([\w+-]+)='
        result = re.findall(regex, word)

        if len(result) > 0:
            l = []
            for elem in result:
                for i in elem:
                    if i:
                        l.append(i)
        D2 = {}
        if len(l) > 1:
            for i in range(1, len(l)):
                    D2.setdefault(l[0], []).append(l[i])
        else:
            D2 = {l[0]: []}
        D1.update(D2)
        continue

for key in sorted(D1):
    print(f'{key}:', end=' ')
    print(*sorted(D1[key]), sep=', ')
