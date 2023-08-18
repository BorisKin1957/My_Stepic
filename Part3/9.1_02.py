'''
Функция convert()

Реализуйте функцию convert(), которая принимает один аргумент:

    number — целое число

Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:

    двоичное представление числа number в виде строки без префикса 0b
    восьмеричное представление числа number в виде строки без префикса 0o
    шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x

Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию convert(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

print(convert(15))

Sample Output 1:

('1111', '17', 'F')

Sample Input 2:

print(convert(-24))

Sample Output 2:

('-11000', '-30', '-18')

Sample Input 3:

print(convert(1))

Sample Output 3:

('1', '1', '1')

Верно. Так держать! '''


def convert(number):
    if number >= 0:
        return (bin(number)[2:], oct(number)[2:], hex(number)[2:].upper())
    return ('-' + bin(number)[3:], '-' + oct(number)[3:], '-' + hex(number)[3:].upper())


print(convert(15))
print(convert(-24))

'''НАДО

def convert(number):
    return (bin(number).replace('0b', ''), oct(number).replace('0o', ''), hex(number).replace('0x', '').upper())
    
    '''
