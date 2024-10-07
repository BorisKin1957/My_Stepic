'''Анализ продаж

К вам в руки попал файлик формата json , в котором содержится информация одного автосалона о продажах менеджеров.
В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого автомобиля.

Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж.
В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.'''

import json

with open('manager_sales.json') as file:
    total, out_l = 0, {}
    data = json.load(file)
    for elem in data:
        for item in elem['cars']:
            total += item['price']
        key = f'{elem['manager']['first_name']} {elem['manager']['last_name']}'
        out_l[key] = total
        total = 0
    result = sorted(out_l.items(), key=lambda x: x[1], reverse=True)
    print(result[0][0], result[0][1])