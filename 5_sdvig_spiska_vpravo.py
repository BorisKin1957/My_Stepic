s = [i  for i in range(1, 6)]
step = 7
while len(s) > 1:
    for i in range(step - 1):
        tmp = []
        tmp.append(s[-1])
        for j in range(len(s) - 1):
            tmp.append(s[j])
        s = tmp[1:]

print(s)