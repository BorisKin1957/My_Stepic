'''
FAKE NEWS 🌶️

Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
Напишите программу, которая принимает на вход текущие дату и время и определяет,
сколько времени осталось до выхода курса.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса,
в следующем формате:

До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов

Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут

Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично,
если количество часов равно нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:

Курс уже вышел!

Примечание 1. Программа должна подбирать правильную форму для существительных «день» и «минута».
Для этого можете смело взять свою функцию choose_plural() из этой задачи.

Sample Input 1:
16.11.2021 06:30

Sample Output 1:
До выхода курса осталось: 357 дней и 5 часов

Sample Input 2:
6.11.2022 12:00

Sample Output 2:
До выхода курса осталось: 2 дня

Sample Input 3:
08.11.2022 10:30

Sample Output 3:
До выхода курса осталось: 1 час и 30 минут

Sample Input 4:
08.11.2022 09:00

Sample Output 4:
До выхода курса осталось: 3 часа

Sample Input 5:
08.11.2022 11:40

Sample Output 5:
До выхода курса осталось: 20 минут

Sample Input 6:
08.11.2022 12:15

Sample Output 6:
Курс уже вышел!

'''

def plural(num, word_shit): # правильное склонение: 5 дней, а не 5 день
    if str(num)[-1] == '1' and len(str(num)) == 1 \
            or str(num)[-1] == '1' and str(num)[-2] != '1':
        result = f'{num} {word_shit[0]}'
    elif str(num)[-2:] in ['11', '12']:
        result = f'{num} {word_shit[2]}'
    elif str(num)[-1] in '234':
        result = f'{num} {word_shit[1]}'
    else:
        result = f'{num} {word_shit[2]}'

    return result


from datetime import datetime

word_d = ('день', 'дня', 'дней')
word_h = ('час', 'часа', 'часов')
word_m = ('минута', 'минуты', 'минут')

today = datetime.strptime(input(), '%d.%m.%Y %H:%M')
curs_day = datetime(2022, 11, 8, 12)
delta = curs_day - today

days = delta.days
hours = delta.seconds // 3600
minutes = delta.seconds % 3600 // 60

if curs_day > today:
    if days and hours:  # days & hours
        print(f'До выхода курса осталось: {plural(str(days), word_d)} и {plural(str(hours), word_h)}')
    elif days and not hours:  # only days
        print(f'До выхода курса осталось: {plural(str(days), word_d)}')
    elif not days and hours and minutes:  # hours & minutes
        print(f'До выхода курса осталось: {plural(str(hours), word_h)} и {plural(str(minutes), word_m)}')
    elif not days and hours and not minutes:  # only hours
        print(f'До выхода курса осталось: {plural(str(hours), word_h)}')
    elif not days and not hours and minutes:  # only minutes
        print(f'До выхода курса осталось: {plural(str(minutes), word_m)}')
else:
    print('Курс уже вышел!')