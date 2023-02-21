poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
sp = list(poet_data)
sp[2] = 'Москва'
poet_data = tuple(sp)

print(poet_data)