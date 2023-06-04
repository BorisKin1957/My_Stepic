'''
Шахматы были лучше 🌶️

Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько
JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}

У футболиста имеются следующие атрибуты:

    first_name — имя
    last_name — фамилия
    team — название футбольного клуба
    position — игровая позиция

Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии
футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в
лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий,
каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует,
что он является корректным текстовым файлом в формате JSON. Для того чтобы определить,
является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией
try-except и функцией is_correct_json() из предыдущего урока.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...

Примечание 3. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
'''

def correct_json(json_data):
    with open(json_data, encoding='utf-8') as file:
        try:
            data = json.load(file)
            return data
        except:
            return False


import json
from zipfile import ZipFile

players = []
with ZipFile('data.zip') as zip_file:
    info = zip_file.namelist()
    for i in info:
        if i.split('.')[-1] == 'json':
            i_ = 'tmp/' + i
            zip_file.extract(i, path='tmp/')
            data = correct_json(i_)
            if data:
                players.append(data)

players = filter(lambda x: x['team'] == 'Arsenal', players)

arsenal = []
for player in players:
    arsenal.append((player['first_name'], player['last_name']))

arsenal = sorted(arsenal, key=lambda x: (x[0], x[1]))

for player in arsenal:
    print(*player)