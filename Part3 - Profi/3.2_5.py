'''Две даты

Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD),
каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в
формате DD-MM (YYYY).

Примечание. Тестовые данные доступны по ссылкам:

Sample Input 1:
2021-05-12
2021-05-04

Sample Output 1:
04-05 (2021)

'''

from datetime import date
l_out = []
for _ in range(2):
    l = input().split('-')
    my_d = date(int(l[0]), int(str(l[1].lstrip('0'))), int(l[2]))
    l_out.append(my_d)
print(min(l_out).strftime('%d-%m (%Y)'))

'''КАК ЛУЧШЕ

from datetime import date

date1 = date.fromisoformat(input())
date2 = date.fromisoformat(input())

print(min(date1, date2).strftime('%d-%m (%Y)'))'''