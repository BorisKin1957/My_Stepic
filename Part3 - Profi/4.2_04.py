'''
Средняя зарплата

Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников
в различных компаниях. В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:

company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...

Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и
выводит их названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты,
они должны быть расположены в лексикографическом порядке их названий.

Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат к их количеству.

Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 4. Начальная часть ответа выглядит так:

Информзащита
Форс
OFT group
...

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv

with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    rows = sorted(list(rows)[1:])
# лабаем библиотеку вида: {company: [sum, count]}, где sum - все деньги на з\п, count - все принятые
    lib, count = {}, 1
    for row in rows:
        key = row[0]
        value = [int(row[1]), count]
        if key in lib:
            count += 1
            lib[key] = [lib[key][0] + value[0], count]
        else:
            count = 1
            lib[key] = value
# делаем сортрованный по средней з\п список вида: [(company, з\п)]
    new = []
    for key, val in lib.items():
        new.append((key, int(val[0] / val[1])))
        new = sorted(new, key=lambda x: x[1])

    print(*[i[0] for i in new], sep='\n')

'''ПРАВИЛЬНО

import csv
d = {}
with open('salary_data.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    for key, value in rows[1:]:
        d[key] = d.get(key, []) + [int(value)]
    
    будет библиотека, вида: {'Atos': [135000, 91000, 58900, 84400, 42900, 55100, 15400....

    d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
    print(*d_sort, sep='\n')
    
    '''