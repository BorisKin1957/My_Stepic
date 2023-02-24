'''Дополните приведенный код так, чтобы в переменной result хранился словарь,
в котором для каждого символа строки text будет подсчитано количество его вхождений.

Примечание. Выводить содержимое словаря result не нужно.'''

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for key in text:
    if key not in result:
        result[key] = text.count(key)

#print(result)