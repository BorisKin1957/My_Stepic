'''Функция num_of_sundays()

Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

    year — натуральное число, год

Функция должна возвращать количество воскресений в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию num_of_sundays(),
но не код, вызывающий ее.

Sample Input 1:
print(num_of_sundays(2021))

Sample Output 1:
52

Sample Input 2:
year = 2000
print(num_of_sundays(year))

Sample Output 2:
53
'''

from datetime import date

def num_of_sundays(y):
    delta = date(y + 1, 1, 1) - date(y, 1, 1)
    dif = date(y, 1, 1).weekday()
    return (delta.days + dif) // 7

print(num_of_sundays(768))

'''ЛУЧШЕЕ

def num_of_sundays(year: int):
    return date(year, 12, 31).strftime('%U')
    
'''