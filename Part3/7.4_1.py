'''
Функция get_weekday()

Реализуйте функцию get_weekday(), которая принимает один аргумент:

    number — целое число (от 11 до 77 включительно)

Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:

    если number не является целым числом, функция должна возбуждать исключение:

    TypeError('Аргумент не является целым числом')

    если number является целым числом, но не принадлежит отрезку [1;7], функция должна возбуждать исключение:

    ValueError('Аргумент не принадлежит требуемому диапазону')

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_weekday(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(get_weekday(1))

Sample Output 1:

Понедельник

Sample Input 2:

try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))

Sample Output 2:

Аргумент не является целым числом
<class 'TypeError'>

Sample Input 3:

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))

Sample Output 3:

Аргумент не принадлежит требуемому диапазону
<class 'ValueError'>

'''

def get_weekday(number):
    if type(number) != int:
        raise TypeError('Аргумент не является целым числом')
    elif not 0 < number < 8:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота",
                7: "Воскресенье", }
        return week[number]


try:
    print(get_weekday(8))
except Exception as err:
    print(err)
    print(type(err))
