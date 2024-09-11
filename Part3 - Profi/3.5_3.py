'''
Снова не успел

Дан режим работы магазина:
Понедельник 	9:00 - 21:00
Вторник 	9:00 - 21:00
Среда 	9:00 - 21:00
Четверг 	9:00 - 21:00
Пятница 	9:00 - 21:00
Суббота 	10:00 - 18:00
Воскресенье 	10:00 - 18:00

Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия магазина.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести количество минут, которое осталось до закрытия магазина, или текст Магазин не работает, если он закрыт.


Sample Input 1:
01.11.2021 20:45

Sample Output 1:
15

Sample Input 2:
02.11.2021 21:15

Sample Output 2:
Магазин не работает

Sample Input 3:
07.11.2021 10:00

Sample Output 3:
480

'''

from datetime import datetime

start0, start1 = datetime(1, 1, 1, 9, 0), datetime(1, 1, 1, 10, 0)
end0, end1 = datetime(1, 1, 1, 21, 0), datetime(1, 1, 1, 18, 0)

s = input()
now = datetime(int(s[6:11]), int(s[3:5]), int(s[:2]), int(s[11:13]), int(s[-2:]))

if (0 <= now.weekday() <= 5 and (now.time() < start0.time() or now.time() >= end0.time())) or \
        (5 <= now.weekday() <= 6 and (now.time() < start1.time() or now.time() >= end1.time())):
    print('Магазин не работает')
else:
    if 0 <= now.weekday() <= 5:
        print((end0 - now).seconds // 60)
    else:
        print((end1 - now).seconds // 60)