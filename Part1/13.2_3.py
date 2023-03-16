'''
Сумма цифр

Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
Тестовые данные 🟢

Sample Input 1:
12345

Sample Output 1:
15
'''


# объявление функции
def print_digit_sum(num):
    print(sum([int(str(num)[i]) for i in range(len(str(num)))]))


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
