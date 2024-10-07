def gen_fibonacci_numbers(n):
    a, b = 0, 1
    for i in range(n):
        result = a + b
        yield result
        a, b = result, a

for i in gen_fibonacci_numbers(10):
    print(i)