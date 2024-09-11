'''
Функция scrabble()

Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:

    symbols — набор символов
    word — слово

Функция должна возвращать True, если из набора символов symbols можно составить слово word,
или False в противном случае.

Примечание 1. При проверке учитывается количество символов, которые нужны для составления слова,
и не учитывается их регистр.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию scrabble(),
но не код, вызывающий ее.


Sample Input 1:
print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))

Sample Output 1:
True

Sample Input 2:
print(scrabble('begk', 'beegeek'))

Sample Output 2:
False

Sample Input 3:
print(scrabble('beegeek', 'beegeek'))

Sample Output 3:
True

'''


def scrabble(simbols, word):
    return Counter(simbols.lower()) & Counter(word.lower()) == Counter(word.lower())


from collections import Counter

print(scrabble('beegeek', 'beegeek'))
