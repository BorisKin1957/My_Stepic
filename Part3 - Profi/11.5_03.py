'''

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют последовательности символов, удовлетворяющие следующим условиям:

    последовательность должна состоять только из bee и geek
    последовательность должна содержать хотя бы один geek
    bee не может находиться рядом с самим собой (не может быть beebee)
    geek может появиться только после того, как до этого было записано bee
    после каждого bee когда-нибудь должен появиться geek

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

Correct name is beegeekbeegeek

Sample Output 1:

beegeekbeegeek

Sample Input 2:

hello beegeek_cyber_school

Sample Output 2:

beegeek

Sample Input 3:

beebeegeekgeekgeekbee

Sample Output 3:

beegeekgeekgeek

Верно решили 920 учащихся
Из всех попыток 34% верных
Прекрасный ответ. '''

regex = r'((bee){1}(geek)+)+'

'''ТОЧНЕЕ

regex = r'(bee(geek)+)+'

'''