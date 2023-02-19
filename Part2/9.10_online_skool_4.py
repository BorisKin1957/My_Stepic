set1 = {i for i in input().split()}
set2 = {i for i in input().split()}

print(*sorted(set1 | set2))