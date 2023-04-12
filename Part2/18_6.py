'''Forbidden words 🌶️

На вход программе подается строка текста с именем текстового файла.
Напишите программу, выводящую на экран содержимое этого файла, но с заменой всех
запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).
Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле
forbidden_words.txt. Гарантируется, что все слова в этом файле записаны в нижнем регистре.
Формат входных данныхНа вход программе подается строка текста с именем существующего
текстового файла, в котором необходимо заменить запрещенные слова звездочками.
Формат выходных данныхПрограмма должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались,
даже если они встречаются в середине другого слова.
Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра.

Например, если файл forbidden_words.txt содержит запрещенное слово exam,
то слова exam, Exam, ExaM, EXAM и подобные должны быть заменены на ****.
Примечание 3. Если бы файл forbidden_words.txt содержал слова:
hello email python the exam wor is
а файл в котором заменяются слова имел бы вид:
Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!
то результатом будет:
*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!

Примечание 4. Файл forbidden_words.txt можно скачать по ссылке.
Ваша программа прогоняется на трех файлах data.txt, stepik.txt и beegeek.txt.'''

'''НЕ ПРИНЯЛ РЕШЕНИЕ

with open('forbidden_words.txt') as f, open(input()) as fn:
    rpnz = f.read().strip().split()
    for line in fn:
        l = line.split(' ') # пробел указан с чужой подсказки! ((
        for bad_word in rpnz:
            new_l = []
            for word in l:
                s = word.lower()
                if bad_word in s:
                    new_word = s.replace(bad_word, '*' * len(bad_word))
                    new_l.append(new_word)
                else:
                    new_l.append(word)
                l = new_l[:]
        print(*new_l, end='')
'''

with open('forbidden_words.txt') as f, open(input()) as fn:
    rpnz = f.read().strip().split()
    txt = fn.read()
    txt_l = txt.lower()
    for bad_word in rpnz:
        txt_l = txt_l.replace(bad_word, '*' * len(bad_word))
    for i in range(len(txt)):
        if txt_l[i] not in '*':
            print(txt[i], end='')
        else:
            print('*', end='')