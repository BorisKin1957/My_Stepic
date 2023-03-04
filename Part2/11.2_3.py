'''
Scrabble game

В игре Scrabble каждая буква приносит определенное количество баллов.
бщая стоимость слова – сумма баллов его букв. Чем реже буква встречается, тем больше она ценится:
Баллы 	Буква
11 	AA, EE, II, LL, NN, OO, RR, SS, TT, UU
22 	DD, GG
33 	BB, CC, MM, PP
44 	FF, HH, VV, WW, YY
55 	KK
88 	JJ, XX
1010 	QQ, ZZ

Напишите программу подсчета итоговой стоимости введенного слова.

Формат входных данных
На вход программе подается одно слово в верхнем регистре на английском языке.

Формат выходных данных
Программа должна вывести суммарную стоимость букв введеного слова.

Примечание. Подробнее про игру можно почитать тут.


Sample Input 1:
DANSER

Sample Output 1:
7

Sample Input 2:
FRESHENER

Sample Output 2:
15

Sample Input 3:
ZIP

Sample Output 3:
14
'''


scr = {1: 'AEILNORSTU',
       2: 'DG',
       3: 'BCMP',
       4: 'FHVWY',
       5: 'K',
       8: 'JX',
       10: 'QZ'
       }

result = sum([k for i in input() for k, v in scr.items() if i in v])

print(result)


# sum = 0
# s = input()
# for i in s:
#     for k, v in scr.items():
#            if i in v:
#               sum += k
# print(sum)