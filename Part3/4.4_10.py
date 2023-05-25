'''
Я исповедую Python, а ты?

Вам доступен файл countries.json, содержащий список JSON-объектов c информацией
о странах и исповедуемых в них религиях:

[
   {
      "country": "Afghanistan",
      "religion": "Islam"
   },
   {
      "country": "Albania",
      "religion": "Islam"
   },
   ...
]

Каждый объект из этого списка содержит два атрибута:

    country — страна
    religion — исповедуемая религия

Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа
название религии, а в качестве значения — список стран, в которых исповедуется данная религия.
Полученный JSON-объект программа должна записать в файл religion.json.

Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

Примечание 2. Начальная часть файла religion.json выглядит так:

{
   "Islam":[
      "Afghanistan",
      "Albania",
      "Algeria",
      ...
   ],
   ...
}

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''

import json

with open('countries.json', encoding='utf-8') as file_in:
    data = json.load(file_in)

religion = {}
for i in data:
    key = i['religion']
    value = i['country']
    if key not in religion:
        religion[key] = religion.get(key, [value])  # если значени нет, получаем значение(value) для ключа key в виде списка [value]
    else:
        religion[key].append(value)  # если уже есть, дополняем списк новым значением + [value]

with open('religion.json', 'w', encoding='utf-8') as file_out:
    json.dump(religion, file_out, indent=3)