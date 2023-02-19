m, n = int(input()), int(input())

set_all = {input() for _ in range(m + n)}

result = m + n - 2 * (m + n - len(set_all))

if result == 0:
    print('NO')
else:
    print(result)

