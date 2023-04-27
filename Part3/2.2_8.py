'''
Корпоративная почта 🌶️

В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая
формируется как <имя-фамилия>@beegeek.bzz, например, timyr-guev@beegeek.bzz. П
ри таком подходе существует проблема тёзок. Для решения такой проблемы
было решено приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера),
второй — timyr-guev1@beegeek.bzz, третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых
сотрудников в заранее подготовленном виде (латиницей с символом - между ними).
Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число n —
количество выданных ящиков. В следующих nn строках перечислены сами ящики в
порядке выдачи, по одному на строке. На следующей строке задано целое
неотрицательное число mm — количество новых сотрудников, которым нужно
раздать корпоративные ящики. Каждая из последующих mm строк представляет
собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (mm строк) для новых сотрудников в том порядке,
в котором они раздавались.

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3
ivan-ivanov
petr-petrov
petr-ivanov

Sample Output 1:
ivan-ivanov3@beegeek.bzz
petr-petrov@beegeek.bzz
petr-ivanov1@beegeek.bzz

Sample Input 2:

2
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3
timyr-guev
timyr-guev
anri-tabuev

Sample Output 2:

timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz

'''

def name_num(s):
    s = s[:s.index('@')]
    num_s, alpha_s = '', ''
    for char in s:
        if char.isdigit():
            num_s += char
        elif char.isalpha() or char == '-':
            alpha_s += char
    if num_s:
            return [alpha_s, num_s]
    return [alpha_s, '0']

# база фамилий компании
beegeek = {}
# предельное значение однофамильцев
limit = 33

for mail in range(int(input())):
    s = input()
    name, num = name_num(s)[0], name_num(s)[1]
    beegeek[name] = beegeek.get(name, [str(i) for i in range(limit)])
    beegeek[name].remove(num)

for mail in range(int(input())):
    name = input()
    if name in beegeek:
        beegeek[name] = beegeek.get(name, [])
        if beegeek[name][0] == '0':
            print(f'{name}@beegeek.bzz')
        else:
            print(f'{name}{beegeek[name][0]}@beegeek.bzz')
        beegeek[name].remove(beegeek[name][0])
    else:
        beegeek[name] = beegeek.get(name, [str(i) for i in range(limit)])
        print(f'{name}@beegeek.bzz')

'''
Вот такое громоздкое решение, в котором базой фамилий является не список, 
или множество, как все делали (и правильно!), 
а словарь имён со свободными номерами в пределах изначально заданного лимита.
Этот лимит - недостаток решения. 
Однако если изменить условия задачи, как то: присваивать номера не последовательно, 
а случайным выбором из ряда чисел, то этот недостаток превратится в достоинство. )

ВОТ КАК НАДО было

emails = set(input() for _ in range(int(input())))
for _ in range(int(input())):
    emp = input()
    email = f'{emp}@beegeek.bzz'
    count = 0
    while email in emails:
        count += 1
        email = f'{emp}{count}@beegeek.bzz'
    emails.add(email)
    print(email)
'''