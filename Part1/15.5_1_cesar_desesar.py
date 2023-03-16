'''Шифр Цезаря

Описание проекта: требуется написать программу, способную шифровать и
дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:

    направление: шифрование или дешифрование;
    язык алфавита: русский или английский;
    шаг сдвига (со сдвигом вправо).

Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст:
"Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

Составляющие проекта:

    Целые числа (тип int);
    Модульная арифметика;
    Переменные;
    Ввод / вывод данных (функции input() и print());
    Условный оператор (if/elif/else);
    Цикл for/while;
    Строковые методы.'''



'''
Функция принимает русскую строку и определяет во сколько раз совокупная частота букв
(о, е, а, и, н, т, с) больше совокупности букв (ь, г, з, б, з, ч, ж)
'''


def freq_ru_chars(stroke):
    s = []
    stroke = stroke.lower()
    s.extend(stroke)
    count_max = s.count('о') + s.count('е') + s.count('а') + s.count('и') + s.count('н') + s.count('т') + s.count('р')
    count_min = s.count('ж') + s.count('ш') + s.count('ц') + s.count('щ') + s.count('ф') + s.count('э') + s.count('х')
    freq = round(count_max / (count_min + 0.01), 3)

    return freq


'''
Функция принимает английскую строку и определяет во сколько раз совокупная частота букв
(a, c, t, o, n) больше совокупности букв (j, k, q, x, z)
'''


def freq_en_chars(stroke):
    s = []
    stroke = stroke.lower()
    s.extend(stroke)
    count_max = s.count('e') + s.count('o') + s.count('t') + s.count('s') + s.count('n') + s.count('a') + s.count('i')
    count_min = s.count('j') + s.count('k') + s.count('q') + s.count('x') + s.count('z') + s.count('v')# + s.count('ж')
    freq = round(count_max / (count_min + 0.01), 3)

    return freq


'''
Функция принимает строку (s) и сдвигает вправо символы на значение (n)
сохраняя на выходе знаки препинания, пробелы, цифры, и регистр символов.
Для строки на русском должны быть переданы параметры:
right = 1103, len_alf = 32
Для строки на английском должны быть переданы параметры:
right = 122, len_alf = 26
'''


def cesar_plus(s, n, right, len_alf):
    stroke = ''
    for i in s:
        if i in ' ,.!-—;:? "0123456789':
            stroke += i
        elif i == i.upper():
            a = ord(i.lower()) + n
            if a > right:
                a -= len_alf
            stroke += chr(a).upper()
        else:
            a = ord(i) + n
            if a > right:
                a -= len_alf
            stroke += chr(a)

    return stroke


'''
Функция дешифрует строку S, когда сдвиг не известен, 
принимая в качестве второго параметра длину алфавита len_alf, 
и lng - как указатель языка (ru/en)
'''


def de_cesar(s, len_alf, lng):
    s_freq = []
    if lng == 'ru':
        right = 1103
        len_alf = 32
        for i in range(33):
            stroke = cesar_plus(s, i, 1103, 32)
            freq = freq_ru_chars(stroke)
            s_freq.append(freq)

    elif lng == 'en':
        right = 122
        len_alf = 26
        for i in range(27):
            stroke = cesar_plus(s, i, 122, 26)
            freq = freq_en_chars(stroke)
            s_freq.append(freq)
    max_freq = max(s_freq)
    ind_freq_max = s_freq.index(max_freq)
    old_stroke = stroke
    for j in range(1, 6):
        max_freq = max(s_freq)
        ind_freq = s_freq.index(max_freq)
        del s_freq[ind_freq]
        s_freq.insert(ind_freq, 0.0)
        stroke = cesar_plus(old_stroke, ind_freq, right, len_alf)
        print('Вариант', j, 'при частоте', max_freq, '˃', stroke)

    stroke = cesar_plus(old_stroke, ind_freq_max, right, len_alf)
    return stroke


'''
ОСНОВНАЯ ПРОГРАММА
'''

print('''
ШИФР ЦЕЗАРЯ

Программа способна шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
Дешифровние производится, в том числе, и без знания кода шифрования. 
При таком дешифрования точность напрямую зависит от длины строки зашифрованного текста.
При длине строки менее 20 знаков она, прямо скажем, никакая )

Поясните следующие данные:
''')

ln = ''
while ln.lower() != 'y' and ln.lower() != 'n':
    ln = input('Язык будет русский (Y) или английский (N) [ Y/N ]: ')

if ln.lower() == 'y':
    lng, right, len_alf = 'ru', 1103, 32
    print('Ваш выбор: РУССКИЙ', end='\n\n')
elif ln.lower() == 'n':
    lng, right, len_alf = 'en', 122, 26
    print('Ваш выбор: АНГЛИЙСКИЙ', end='\n\n')

ln = ''
while ln.lower() != 'y' and ln.lower() != 'n':
    ln = input('Задайте направление: шифрование (Y) или дешифрование (N) [ Y/N ]: ')

if ln.lower() == 'y':
    choice = 'cesar'
    print('Ваш выбор: ШИФРОВАНИЕ', end='\n\n')
elif ln.lower() == 'n':
    choice = 'de_cesar'
    print('Ваш выбор: ДЕШИФРОВАНИЕ', end='\n\n')

stroke = input('Введите текст: ')

if choice == 'cesar':
    n = ''
    while n.isdigit() == False:
        n = input('Задайте численное значение сдвига шифрования: ')
    n = int(n)
    stroke = cesar_plus(stroke, n, right, len_alf)

elif choice == 'de_cesar':
    ln = ''
    while ln.lower() != 'y' and ln.lower() != 'n':
        ln = input('Вам известен код шифра? [ Y/N ]: ')
    if ln.lower() == 'y':
        n = 0
        while n == 0 and str(n):
            n = int(input('Введите его значение: '))
            n = len_alf - n
            stroke = cesar_plus(stroke, n, right, len_alf)
    else:
        stroke = de_cesar(stroke, len_alf, lng)

print('\n', 'ВЫВОЖУ РЕЗУЛЬТАТ: ', stroke, sep='')