'''ТУЧА ЦИКЛОВ в пустую'''
def sdvig_number(numbers, i):
    new = numbers[:i] + numbers[i + 1:] + numbers[i:i + 1]
    return new

def ret_number(numbers):

    new1 = numbers[-1:]
    new2 = numbers[:-1]
    return new1 + new2


def res_numbers(numbers):
    bigest = 0
    lenght = len(numbers)
    for i in range(lenght):
        for j in range( lenght - i):
            num = int(''.join(numbers))
            if num >= bigest:
                bigest = num
                res_numbers = numbers[:]
            numbers = ret_number(numbers[:])

        numbers = sdvig_number(numbers[:], i)


    return res_numbers


def get_biggest(numbers):
    if numbers:
        result = []

        numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            numbers = res_numbers(numbers)[:]
            result.append(numbers[0])
            numbers = numbers[1:]
            print(f'До конца осталось {len(numbers)}циклов')
            print(result  )
#        return int(''.join(result))
        return result
    return -1

#print(get_biggest([61, 228, 9, 3, 11]))

#print(get_biggest([i for i in range(1000)]))

with open('15.txt') as f_result, open('15_in.txt') as f_input:
    good = int(f_result.read())
    in_list = f_input.read().split(', ')
    num_list = [int(i) for i in in_list]
    if good == get_biggest(num_list):
        print('Yes')
    else:
        print('No')
