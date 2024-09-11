'''
Only numbers

На вход программе подается неопределенное количество строк, каждая из которых содержит произвольное значение.
Напишите программу с использованием конструкции try-except, которая выводит сумму всех введенных чисел,
а затем — количество введенных нечисловых значений.

Формат входных данных
На вход программе подается неопределенное количество строк (хотя бы одна),
каждая из которых содержит произвольное значение.

Формат выходных данных
Программа должна вывести сумму всех введенных чисел (тип int и float), а затем на следующей строке —
количество введенных нечисловых значений.

Примечание 1. Если ни одно число введено не было, то сумма равна 00.

Примечание 2. Рассмотрим первый тест. Имеем три введенных числа, сумма которых равна:
100+10+1.1=111.1
100+10+1.1=111.1Также три нечисловых значения, а именно: i'm number!, [1, 99], {'math', 'physics'}.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

100
i'm number!
10
[1, 99]
1.1
{'math', 'physics'}

Sample Output 1:

111.1
3

Sample Input 2:

10
10

Sample Output 2:

20
0

Sample Input 3:

abc
cda
xyz

Sample Output 3:

0
3

'''

import sys

total, count = 0, 0

for i in sys.stdin:
    try:
        total += float(i)
    except ValueError:
        count += 1

if total == int(total):
    print(int(total))
else:
    print(total)

print(count)

'''НАДО ТАК

import sys
s, counter = 0, 0
for line in sys.stdin:
    try:
        s += int(line)
    except ValueError:
        try:
            s += float(line)
        except ValueError:
            counter += 1
print(s)
print(counter)
'''
