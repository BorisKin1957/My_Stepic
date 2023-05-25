'''
Результаты экзамена 🌶️

Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором
учебном заведении. В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка
за экзамен, в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:

name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...

Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле
до трёх раз с различной оценкой и различными датой и временем сдачи.

Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и
время ее получения. Программа должна создать список словарей, каждый из которых содержит следующие
пары ключ-значение:

    name — имя студента
    surname — фамилия студента
    best_score — максимальная оценка за экзамен
    date_and_time — дата и время получения максимальной оценки в исходном формате
    email — адрес электронной почты

Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть
расположены в лексикографическом порядке названий электронных почт.

Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве даты следует
указать дату пересдачи.

Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, при этом кавычки не используются.

Примечание 3. Начальная часть файла best_scores.json выглядит так:

[
   {
      "name": "Stephen",
      "surname": "Farley",
      "best_score": 3,
      "date_and_time": "2021-11-12 12:00:00",
      "email": "aardo@mac.com"
   },
   {
      "name": "Kaylen",
      "surname": "Horne",
      "best_score": 4,
      "date_and_time": "2021-11-09 11:00:00",
      "email": "aaribaud@att.net"
   },
   ...
]

Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json, csv
from datetime import datetime

with open('exam_results.csv', encoding='utf-8', newline='') as file_in:
    rows = list(csv.reader(file_in, delimiter=';'))

columns = rows[0]
data = rows[1:]
data = sorted(data, key=lambda x: x[0].split(',')[-1])

all = []
keys = ('name', 'surname', 'best_score', 'date_and_time', 'email')
for line in data:
    l = line[0].split(',')
    name, surname, score, date_and_time, email = l[0], l[1], int(l[2]), datetime.strptime(l[-2], '%Y-%m-%d %H:%M:%S'), \
    l[-1]

    flag = True
    D = dict(zip(keys, (name, surname, score, date_and_time, email)))

    for j in all:
        if j['email'] == D['email']:
            flag = False
            if (j['best_score'] < D['best_score']) or (
                    j['best_score'] == D['best_score'] and j['date_and_time'] < D['date_and_time']):
                j['best_score'] = D['best_score']
                j['date_and_time'] = D['date_and_time']
        else:
            flag = True
    if flag:
        all.append(D)

for i in all:
    i['date_and_time'] = str(i['date_and_time'])

with open('best_scores.json', 'w', encoding='utf-8') as file_out:
    json.dump(all, file_out, indent=3)