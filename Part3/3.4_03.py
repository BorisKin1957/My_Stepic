'''Предыдущая и следующая даты

Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.

Формат входных данных
На вход программе подается дата в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести предыдущую и следующую даты относительно
введенной даты, каждую на отдельной строке, в формате DD.MM.YYYY.

Примечание 1. Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.'''

from datetime import date, timedelta

pat = '%d.%m.%Y'
day = input().split('.')

now = date(day=int(day[0]), month=int(day[1]), year=int(day[2]))

before = now - timedelta(days=1)
next = now + timedelta(days=1)

print(before.strftime(pat), next.strftime(pat), sep='\n')