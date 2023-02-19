m, n = int(input()), int(input())

set1 = {input() for _ in range(m)}
set2 = {input() for _ in range(n)}

if set1 == set2:
    print('NO')
else:
    print(m + n - 2 * len(set1 & set2))

# if len(set1 - set2) + len(set2 - set1) != 0:
#     print(len(set1 - set2) + len(set2 - set1))
# else:
#     print('NO')