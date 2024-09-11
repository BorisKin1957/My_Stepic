'''
Структура архива 🌶️🌶️

Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его
файловую структуру и объем каждого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде.
Так как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.

Примечание 1. Вывод на примере архива test.zip из конспекта:

test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B

Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.

Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:

    1 KB = 1024 B
    1 MB = 1024 KB
    1 GB = 1024 MB

Примечание 4. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
'''


def json_to_str(data_json):
    new = ''
    for sim in data_json:
        if sim not in '{}":,':
            new += sim
    dd = new.replace('\n    ', '\n')
    new = dd.replace('\n\n', '\n')
    dd = new.replace('\n    \n    ', '\n    ')
    new = dd.replace('\n    \n', '\n')
    dd = new.replace('    ', '  ')
    new = dd.replace('\n    \n', '\n')

    return(new.strip('\n'))



import json
from zipfile import ZipFile

with ZipFile('desktop.zip') as zip_file:
    name = zip_file.namelist()
    info = zip_file.infolist()

L = []
for item in name:
    l = item.strip('/').split('/')
    L.append(l)

D = {}

for item in L:
    for i in range(len(item)):
        a = item[i]
        if '.' not in a:
            if i == 0:
                key0 = a
                if a not in D:
                    D.setdefault(a, {})
            elif i == 1:
                key1 = a
                tmp = ', '.join(D[key0])
                if a not in tmp:
                    D[key0].setdefault(a, {})
            elif i == 2:
                key2 = a
                tmp = ', '.join(D[key0][key1])
                if a not in tmp:
                    D[key0][key1].setdefault(a, {})
        else:
            file = '/'.join(item)
            ind = name.index(file)
            size = info[ind].file_size
            if size < 1024:
                b = str(size) + ' B'
            if 1024 <= size < 1024 ** 2:
                b = str(round(size / 1024)) + ' KB'
            if 1024 ** 2  <= size < 1024 ** 3:
                b = str(round(size / 1024 ** 2)) + ' MB'
            if i == 0:
                D.setdefault(a, b)
            if i == 1:
                D[key0].setdefault(a, b)
            if i == 2:
                D[key0][key1].setdefault(a, b)
            if i == 3:
                D[key0][key1][key2].setdefault(a, b)

data = json.dumps(D, indent=4)

print(json_to_str(data))

'''ВЕРНОЕ РЕШЕНИЕ списком

from zipfile import ZipFile


def convert(value):
    if 0 < value < 1024:
        return f'{value} B'
    elif 1024 < value < 1024 ** 2:
        return f'{round(value / 1024)} KB'
    elif 1024 ** 2 < value < 1024 ** 3:
        return f'{round(value / 1024 ** 2)} MB'
    elif 1024 ** 3 < value < 1024 ** 4:
        return f'{round(value / 1024 ** 3)} GB'
    else:
        return ''


with ZipFile('desktop.zip') as zip_file:
    for i in zip_file.infolist():
        a = i.filename.strip('/').split('/')
        name = a[-1]
        print('  ' * (len(a) - 1), end='')
        print(name, convert(i.file_size))'''