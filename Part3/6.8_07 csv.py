'''
Here we go again

Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты,
в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...

Напишите программу, которая определяет, сколько раз пользователь менял имя.
Программа должна вывести адреса электронных почт пользователей, указав для каждого соответствующее количество
смененных имен. Почтовые ящики должны быть расположены в лексикографическом порядке, каждый на отдельной строке,
в следующем формате:

<адрес электронной почты>: <количество изменений имен>

Примечание 1. Начальная часть ответа выглядит так:

barbaraanderson@bk.ru: 3
barbarabrown@rambler.ru: 3
...

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv
from datetime import datetime

pat = '%d/%m/%Y %H:%M'
D = {}
with open('name_log.csv', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for nicname, email, meeting_time in list(rows)[1:]:
        dt = datetime.strptime(meeting_time, pat)
        if email not in D:
            D[email] = [(nicname, dt)]
        else:
            D[email].append((nicname, dt))

D = sorted(D.items(), key=lambda x: x[0])

for item in D:
    print(f'{item[0]}: {len(item[1])}')
