'''День недели

Напишите программу, которая определяет день недели, соответствующий заданной дате.

Формат входных данных
На вход программе подается дата в формате YYYY-MM-DD.

Формат выходных данных
Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.

Sample Input 1:
2021-12-10

Sample Output 1:
Friday'''

from datetime import datetime
import calendar

dt = datetime.strptime(input(), '%Y-%m-%d')

print(list(calendar.day_name)[dt.weekday()])