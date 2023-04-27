def fun(num, lenght):
    bits = len(str(num))
    if bits == 1:
        numer = int(num * lenght )
        return numer
    elif bits == 2:
        if 90 > int(num) >= 88 or 80 > int(num) > 76 or 70 > int(num) > 65 or 60 > int(num) > 54\
                or 50 > int(num) > 43 or 40 > int(num) > 32 or 30 > int(num) > 21 or 20 > int(num) > 10:
            numer = int(num + str(int(num[0]) + 1))
            return numer
        else:
            return int(num + num[0])
    return int(num)


def get_biggest(numbers):
    if numbers:
        numbers = sorted(numbers, reverse=True)
        new = sorted(numbers, key=lambda num: fun(str(num), len(str(numbers[0]))), reverse=True)
        print(new)

        return int(''.join([str(i) for i in new]))
    return - 1
#
# with open('15.txt') as f:
#     good = int(f.read())
#     if good == get_biggest([i for i in range(1000)]):
#         print('Yes')
#     else:
#         print('No')


with open('15.txt') as f_result, open('15_in.txt') as f_input:
    good = int(f_result.read())
    in_list = f_input.read().split(', ')
    num_list = [int(i) for i in in_list]
    if good == get_biggest(num_list):
        print('Yes')
    else:
        print('No')

print(get_biggest([i for i in range(1000)]))