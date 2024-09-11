'''
Функция extract_this()

Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:

    zip_name — название zip архива, например, data.zip
    *args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла

Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано
ни одного названия файла для извлечения, то функция должна извлечь все файлы из архива.

Примечание 1. Например, следующий вызов функции

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')

должен извлечь из архива workbook.zip файлы earth.jpg и exam.txt в папку с программой.

Вызов функции

extract_this('workbook.zip')

должен извлечь из архива workbook.zip все файлы в папку с программой.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию extract_this(),
но не код, вызывающий ее.
'''

def extract_this(zip_name, *args):
    if args:
        for name in args:
            with ZipFile(zip_name, mode='a') as zip_file:
                info = zip_file.namelist()
                for i in info:
                    if i.split('/')[-1] == name:
                        ind = info.index(i)
                        break
                our_file = zip_file.getinfo(info[ind])
                name_file = our_file.filename
                zip_file.extract(name_file)
    else:
        with ZipFile(zip_name, mode='a') as zip_file:
            zip_file.extractall()


from zipfile import ZipFile

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')