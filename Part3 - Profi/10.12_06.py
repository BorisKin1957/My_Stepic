'''
Функция password_gen()

Вам доступна функция password_gen(), которая возвращает генератор, порождающий все трехсимвольные строковые пароли
в порядке возрастания, составленные из цифр от 0 до 9 включительно.

Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию password_gen(),
но не код, вызывающий ее.

Sample Input:

passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))

Sample Output:

000
001
002

Напишите программу. Тестируется через stdin → stdout
Верно решили 954 учащихся
Из всех попыток 81% верных
Хорошая работа. '''

from string import ascii_lowercase
from itertools import product

def password_gen():
    # for i in range(10):
    #     for j in range(10):
    #         for k in range(10):
    #             yield str(i) + str(j) + str(k)

    tmp = product(range(10), repeat=3)
    yield from [f'{i[0]}{i[1]}{i[2]}' for i in tmp]


passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))