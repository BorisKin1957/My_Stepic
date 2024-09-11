'''
Популярные домены

Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...

Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...

где в первом столбце записано название почтового домена, а во втором — количество пользователей,
использующих данный домен. Домены в файле должны быть расположены в порядке возрастания количества
их использований, при совпадении количества использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

domain,count
rambler.ru,24
iCloud.com,29
...

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv

with open('data.csv', encoding='utf-8') as file_in, open('domain_usage.csv', 'w') as file_out:
    rows = list(csv.reader(file_in))[1:]
    lib = {}
    for name, surname, email in rows:
        domain = email.split('@')[1]
        lib[domain] = lib.get(domain, 0) + 1

    new = sorted(lib.items(), key=lambda item: (item[1], item[0]))  # сор-ка по кортежу: сначала число, затем имя

    file_out.write('domain,count\n')
    for email, count in new:
        file_out.write(f'{email},{count}\n')
