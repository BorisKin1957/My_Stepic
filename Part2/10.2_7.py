'''Код Морзе'''


letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

mylist = []

for i in range(len(morse)):
    mylist.append((letters[i], morse[i]))

mydic = dict(mylist)


for i in input():
    if i.isalpha() or i.isdigit():
        if i.isalpha():
            print(mydic[i.upper()], end=' ')
        else:
            print(mydic[i], end=' ')

#  Вот самое верное:
# mydict = dict(zip(letters, morse))
# word = input().upper()
#
# for c in word:
#     if c in mydict:
#         print(mydict[c], end=' ')