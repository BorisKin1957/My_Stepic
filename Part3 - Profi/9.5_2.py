'''
Функция generator_square_polynom()

Рассмотрим семейство функций — квадратных трехчленов. Все эти функции имеют один и тот же вид:
f(x)=ax2+bx+c
f(x)=ax2+bx+cРеализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:

    a — вещественное число, коэффициент aa
    b — вещественное число, коэффициент bb
    c — вещественное число, коэффициент cc

Функция generator_square_polynom() должна возвращать функцию, которая принимает в качестве аргумента вещественное число x и возвращает значение выражения ax2+bx+cax2+bx+c.

Примечание 1. Рассмотрим пример из первого теста. Вызов generator_square_polynom(1, 2, 1) возвращает функцию, соответствующую квадратному трехчлену x2+2x+1x2+2x+1.  Функция присваивается переменной f. Далее полученная функция вызывается с аргументом 55 и возвращает значение 52+5⋅2+1=3652+5⋅2+1=36.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию generator_square_polynom(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

f = generator_square_polynom(1, 2, 1)
print(f(5))

Sample Output 1:

36

Sample Input 2:

print(generator_square_polynom(9, 52, 64)(8))

Sample Output 2:

1056

Sample Input 3:

f = generator_square_polynom(26, 83, 22)
print(f(55))

Sample Output 3:

83237

Правильно, молодец! '''

# def generator_square_polynom(a, b, c):
#     def inner(x):
#         return a * x ** 2 + b * x + c
#     return inner


def generator_square_polynom(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = generator_square_polynom(1, 2, 1)
print(f(5))

print(generator_square_polynom(9, 52, 64)(8))