from datetime import datetime

pat = '%d.%m.%Y'
n, name_lib, count = int(input()), {}, 0

for _ in range(n):
    s = input()
    name, sdt = s[:-11], s[-10:]
    dt = datetime.strptime(sdt, pat)
    if dt in name_lib:
        name_lib[dt] = name_lib.get(dt, [name]) + [name]
    else:
        name_lib[dt] = name_lib.get(dt, [name])

dt_min = min(name_lib)
count = len(name_lib[dt_min])

if count == 1:
    print(f'{dt_min.strftime(pat)} {name_lib[dt_min][0]}')
else:
    print(f'{dt_min.strftime(pat)} {count}')