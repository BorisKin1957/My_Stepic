n = int(input())

myset = {input() for i in range(int(input()))}

for i in range(n - 1):
    myset &= {input() for j in range(int(input()))}

print(*sorted(myset), sep='\n')
