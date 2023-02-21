'''Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
и если в ней присутствует слово "anton" (необязательно рядом стоящи буквы,
главное наличие последовательности букв), то холодильник заражен и нужно
вывести номер холодильника, нумерация начинается с единицы'''


def bad(stroke):
    s, s_ = [], []
    for i in stroke:
        s.append(i)
    for i in 'anton':
        if i in s:
            s = s[s.index(i):]
            s_.append(i)
    if s_ == ['a', 'n', 't', 'o', 'n']:
        return True
    else:
        return False

n = int(input())
bad_num = []

for i in range(1, n + 1):
    if bad(input()):
        bad_num.append(i)
print(*bad_num)