'''
Опасный вирус 😈

В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik,
проник опасный вирус и сломал контроль прав доступа к файлам.
Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:
    запись W (write, доступ на запись в файл);
    чтение R (read, доступ на чтение из файла);
    запуск X (execute, запуск на исполнение файла).

Напишите программу для восстановления контроля прав доступа к файлам.
Ваша программа для каждого запроса должна будет возвращать OK
если выполняется допустимая операция, и Access denied, если операция недопустима.

Формат входных данных
Программа получает на вход количество файлов nn, содержащихся в файловой системе компьютера.
Далее идет n строк, на каждой имя файла и допустимые с ним операции, разделенные символом пробела.
В следующей строке записано число m — количество запросов к файлам, и затем m строк
с запросами вида операция файл. Одному и тому же файлу может быть адресовано любое количество запросов.

Формат выходных данных
Программа должна вывести для каждого из mm запросов в отдельной строке Access denied или OK.
Тестовые данные 🟢

Sample Input 1:
5
my_pycode.exe W X
log_n X W R
ave R
lucky_m W R
dnsss.py W
6
execute ave
read dnsss.py
write log_n
execute log_n
read ave
write my_pycode.exe

Sample Output 1:
Access denied
Access denied
OK
OK
OK
OK

Sample Input 2:
2
marvel_movies X
dc_com X R
2
execute dc_com
write dc_com

Sample Output 2:
OK
Access denied

'''

all_dict = {}
for _ in range(int(input())):
    k, *v = input().split()
    all_dict[k] = v

for v in all_dict.values():
    if 'X' in v:
        v.remove('X')
        v.append('E')

for _ in range(int(input())):
    s = input().split()
    if s[0][0].upper() in all_dict[s[1]]:
        print('OK')
    else:
        print('Access denied')