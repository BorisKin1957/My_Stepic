'''НЕ ВЕРНЫЙ Алгоритм
Идея: двигая на 1 позицию числа в списке, искать макимальное.
Как нашел, старшее число списка сохранял.
Затем повторял с остатком списка'''

def ret_number(numbers):

    new1 = numbers[-1:]
    new2 = numbers[:-1]
    return new1 + new2


def res_numbers(numbers):
    bigest = 0
    for i in range(len(numbers)):
        num = int(''.join(numbers))
        if num >= bigest:
            bigest = num
            res_numbers = numbers[:]
        numbers = ret_number(numbers[:])

    return res_numbers


def get_biggest(numbers):
    if numbers:
        result = []

        numbers = sorted(numbers, reverse=True)
        numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            numbers = res_numbers(numbers)[:]
            result.append(numbers[0])
            numbers = numbers[1:]
#        return int(''.join(result))
        return result
    return -1

#print(get_biggest([61, 228, 9, 3, 11]))

print(get_biggest([i for i in range(1000)]))
