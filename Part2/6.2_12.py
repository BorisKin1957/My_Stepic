tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []
for i in tuples:
    if i:
        non_empty_tuples.append(i)

print(non_empty_tuples)
