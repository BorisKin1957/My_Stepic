'''
Ключевые слова

В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов.
Для получения списка всех ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword.

Приведенный ниже код:

import keyword

print(keyword.kwlist)

выводит:

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна в введенном тексте заменить все ключевые слова (в любом регистре) на строку <kw> и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

True, assert, as, false, or, Import

Sample Output 1:

<kw>, <kw>, <kw>, <kw>, <kw>, <kw>

Sample Input 2:

True or False - that's the question

Sample Output 2:

<kw> <kw> <kw> - that's the question

Sample Input 3:

True and False - that is the question

Sample Output 3:

<kw> <kw> <kw> - that <kw> the question

Напишите программу. Тестируется через stdin → stdout
Верно решили 957 учащихся
Из всех попыток 60% верных
Хорошие новости, верно! '''

import re
import keyword

def func_kw():
    list_kw = keyword.kwlist
    string = f'\\b{list_kw[0]}\\b'
    for word in list_kw[1:]:
        string += f'|\\b{word}\\b'
    return string


result = re.sub(func_kw(), '<kw>', input(), flags=re.I)
print(result)


# result = re.sub(r'\bFalse\b|\bNone\b|\bTrue\b|\band\b|\bas\b|\bassert\b|\basync\b|\bawait\b|\bbreak\b|'
#                 r'\bclass\b|\bcontinue\b|\bdef\b|\bdel\b|\belif\b|\belse\b|\bexcept\b|\bfinally\b|\bfor\b|'
#                 r'\bfrom\b|\bglobal\b|\bif\b|\bimport\b|\bin\b|\bis\b|\blambda\b|\bnonlocal\b|\bnot\b|\bor\b|'
#                 r'\bpass\b|\braise\b|\breturn\b|\btry\b|\bwhile\b|\bwith\b|\byield\b', '<kw>', input(), flags=re.I)
#
# print(result)