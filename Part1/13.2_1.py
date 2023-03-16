'''Звездный треугольник

Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

    fill – символ заполнитель;
    base – величина основания равнобедренного треугольника;

а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.

Sample Input 1:
*
9

Sample Output 1:

*
**
***
****
*****
****
***
**
*

'''

# объявление функции
def draw_triangle(fill, base):
    base = base // 2 + 1
    print(*[i * fill for i in range(1, base + 1)], sep='\n')
    print(*[base * fill for base in range(base - 1, 0, -1)], sep='\n')


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)