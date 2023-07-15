'''
Бесплатные курсы берут свое 😢

Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о
продажах за год, разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv.
В каждом файле в первом столбце указывается название продукта, а в последующих — количество проданного
продукта в килограммах за определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...

Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта,
а значением — цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}

Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.

Примечание 1. Ссылки на указанные файлы: quarter1.csv, quarter2.csv, quarter3.csv, quarter4.csv, prices.json.
Ответ на задачу доступен по ссылке.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
'''

from collections import Counter
import csv, json

D, result = {}, 0

L = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']

with open('prices.json', encoding='utf-8') as file:
    prices = json.load(file)

for file_name in L:
    with open(file_name, encoding='utf-8') as csv_file:
        rows = list(csv.reader(csv_file, delimiter=','))[1:]
    for key, m1, m2, m3 in rows:
        D[key] = (int(m1) + int(m2) + int(m3)) * prices[key]
    result += Counter(D).total()

print(result)