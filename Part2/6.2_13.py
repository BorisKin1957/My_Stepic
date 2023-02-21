tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]

new_tuples = [list(i) for i in tuples]

for i in range(len(new_tuples)):
    new_tuples[i][-1] = 100

new_tuples = [tuple(i) for i in new_tuples]

print(new_tuples)