'''
Число сочетаний

Описать рекурсивную функцию get_combin, которая принимает на вход два целых числа  и находит C(N,K) —
число сочетаний из N элементов по K — с помощью рекуррентного соотношения:

При этом гарантируется, что входные значения n и k будут удовлетворять следующим условиям:

    n > 0
    0 ≤ k ≤ n

Вот примеры вызовов:

get_combin(5, 5) => 1
get_combin(5, 2) => 10
get_combin(3, 1) => 3
get_combin(7, 0) => 1

Ваша задача только написать определение функции get_combin

Sample Input 1:

6
3

Sample Output 1:

20

Sample Input 2:

10
7

Sample Output 2:

120

Sample Input 3:

5
2

Sample Output 3:

10

Sample Input 4:

7
3

Sample Output 4:

35

'''

def get_combin(n: int, k:int) -> int:
    return 1 if k == 0 else 1 if n == k else get_combin(n - 1, k) + get_combin(n - 1, k - 1)