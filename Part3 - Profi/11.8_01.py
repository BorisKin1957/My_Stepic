'''
Функция normalize_jpeg()

Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:

    filename — название файла, имеющее расширение jpeg или jpg, которое может быть записано буквами произвольного регистра

Функция должна возвращать новое название файла с нормализованным расширением — jpg.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию normalize_jpeg(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(normalize_jpeg('stepik.jPeG'))

Sample Output 1:

stepik.jpg

Sample Input 2:

print(normalize_jpeg('mountains.JPG'))

Sample Output 2:

mountains.jpg

Sample Input 3:

print(normalize_jpeg('windows11.jpg'))

Sample Output 3:

windows11.jpg

Верно решили 942 учащихся
Из всех попыток 41% верных
Правильно. '''

import re

def normalize_jpeg(text):
    result = re.sub(r'\.[jJ][pP][eE]?[gG]$', r'.jpg', text)

    return result

print(normalize_jpeg('stepik.jPeG'))

print('test 2')
print(normalize_jpeg('mountains.JPG'))

print('test 3')
print(normalize_jpeg('windows11.jpg'))

print('test 4')
print(normalize_jpeg('jepg_file.jPG'))

print('test 5')
print(normalize_jpeg('file_jepg.jPeG'))

print('test 6')
print(normalize_jpeg('file.jepg.JPEG'))

print('test 8')
print(normalize_jpeg('stepik.jpeg.jpeg'))

print('test 9')
print(normalize_jpeg('stepik.jpg.jpeg'))

print('test 10')
print(normalize_jpeg('stepik.jpeg.jpg'))

print('test 11')
print(normalize_jpeg('beegeek.JPg'))

print('test 12')
print(normalize_jpeg('нарусском.JPg'))

print('test 13')
print(normalize_jpeg('на русском языке.JPG'))

print('test 14')
print(normalize_jpeg('jpg.jPg.Jpg.JPG'))