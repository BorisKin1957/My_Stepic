s = [i  for i in range(1, 11)]
step = 5

for i in range(step):
    tmp = []
    for j in range(1, len(s)):
        tmp.append(s[j])
    tmp.append(s[0])
    s = tmp

print(s)