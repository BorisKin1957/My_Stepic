'''Функция csv_columns()

Реализуйте функцию csv_columns(), которая принимает один аргумент:

    filename — название csv файла, например, data.csv

Функция должна возвращать словарь, в котором ключом является название столбца файла filename,
а значением — список элементов этого столбца.

Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая,
при этом кавычки не используются.

Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.

Примечание 3. Например, если бы файл exam.csv имел вид:

name,grade
Timur,5
Arthur,4
Anri,5

то следующий вызов функции csv_columns():

csv_columns('exam.csv')

должен был бы вернуть:

{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}

Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.

Примечание 5. В тестирующую систему сдайте программу, содержащую только необходимую функцию csv_columns(),
но не код, вызывающий ее.

Примечание 6. Тестовые данные доступны по ссылкам:'''


def csv_columns(file):
    with open(file, encoding='utf-8') as file:
        rows = list(csv.reader(file))
        title, dates, lib = rows[0], rows[1:], {}
        for i in range(len(title)):
            lib[title[i]] = []
            for j in dates:
                lib[title[i]].append(j[i])

        return lib


import csv

text = '''movie,year,rating
Machete,2010,72
Marvin's Room,1996,80
Raging Bull,1980,97
This Boy's Life,1993,75
Silver Linings Playbook,2012,92
Taxi Driver,1976,99
Jackie Brown,1997,87
Shark Tale,2004,35
Bang the Drum Slowly,1973,88
Analyze That,2002,27
Meet the Parents,2000,84
Wag the Dog,1997,85
The Big Wedding,2013,7
'''

with open('deniro.csv', 'w') as file:
    file.write(text)

print(csv_columns('deniro.csv'))
