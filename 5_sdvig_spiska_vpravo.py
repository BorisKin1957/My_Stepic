s = [i  for i in range(1, 11)]
step = 1

for i in range(step):
    tmp = []
    tmp.append(s[-1])
    for j in range(len(s) - 1):
        tmp.append(s[j])
    s = tmp

print(s)