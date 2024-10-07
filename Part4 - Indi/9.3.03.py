import json
from pprint import pprint

with open('group_people.json') as file:
    total, out_l = 0, {}
    data = json.load(file)

    for elem in data:
        for item in elem['people']:
            if item['gender'] == 'Female' and item['year'] > 1977:
                key = elem['id_group']
                total += 1
                out_l[key] = total
        total = 0
    result = sorted(out_l.items(), key=lambda x: x[1], reverse=True)
    pprint(result[0])