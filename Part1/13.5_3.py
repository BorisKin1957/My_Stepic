'''Next Prime 🌶️🌶️

Напишите функцию get_next_prime(num), которая принимает в качестве аргумента
натуральное число num и возвращает первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

Примечание 2. Следующий программный код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))

должен выводить:

7
11
17

'''


# объявление функции
def is_prime(num):
    a = True
    if num == 1:
        a = False
    for i in range(2, num):
        if num % i == 0:
            a = False
            break
    return a


def get_next_prime(num):
    num += 1
    while is_prime(num) == False:
        num += 1
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
