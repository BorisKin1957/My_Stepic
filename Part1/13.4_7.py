'''
Merge lists 2

На вход программе подается число n, а затем n строк, с
одержащих целые числа в порядке возрастания.
Из данных строк формируются списки чисел.
Напишите программу, которая объединяет указанные списки
в один отсортированный список с помощью функции quick_merge(), а затем выводит его.

Формат входных данных
На вход программе подается натуральное число n, а затем nn строк,
содержащих целые числа в порядке возрастания, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

3
1 2 3 4
5 6 7
10 11 17

Sample Output 1:

1 2 3 4 5 6 7 10 11 17

'''


def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


n, sort_lst = int(input()), []

for i in range(1, n + 1):
    numbers = input().split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    sort_lst = quick_merge(sort_lst, numbers)

print(*sort_lst)
