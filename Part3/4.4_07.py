'''
Разные типы

Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]

Напишите программу, которая создает список, элементами которого являются объекты из списка,
содержащегося в файле data.json, измененные по следующим правилам:

    если объект является строкой, в его конец добавляется восклицательный знак
    если объект является числом, он увеличивается на единицу
    если объект является логическое значением, он инвертируется
    если объект является списком, он удваивается
    если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
    если объект является пустым значением (null), он не добавляется

Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]

то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)
new = []
for value in data:
    if type(value) == str:
        new.append(value + '!')
    elif type(value) == int:
        new.append(value + 1)
    elif type(value) == bool:
        new.append(not value)
    elif type(value) == list:
        new.append(value * 2)
    elif type(value) == dict:
        value.update({'newkey': None})
        new.append(value)

with open('updated_data.json', 'w', encoding='utf-8') as file_out:
    json.dump(new, file_out, indent=3)