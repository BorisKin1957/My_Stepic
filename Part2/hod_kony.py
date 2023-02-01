'''Ходы коня

На шахматной доске стоит конь. рограммa отмечает положение коня на доске и все клетки, которые бьет конь.
Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *,
остальные клетки заполните точками.
На вход программе подаются координаты коня  в шахматной нотации (то есть в виде e4'''

def chess_(pos, fig):
    matrix = [(' . ' * 8).split() for _ in range(8)]
    if pos[0] == 'a':
        col = 0
    elif pos[0] == 'b':
        col = 1
    elif pos[0] == 'c':
        col = 2
    elif pos[0] == 'd':
        col = 3
    elif pos[0] == 'e':
        col = 4
    elif pos[0] == 'f':
        col = 5
    elif pos[0] == 'g':
        col = 6
    elif pos[0] == 'h':
        col = 7

    if pos[1] == '8':
        row = 0
    elif pos[1] == '7':
        row = 1
    elif pos[1] == '6':
        row = 2
    elif pos[1] == '5':
        row = 3
    elif pos[1] == '4':
        row = 4
    elif pos[1] == '3':
        row = 5
    elif pos[1] == '2':
        row = 6
    elif pos[1] == '1':
        row = 7


    matrix[row][col] = fig

    if fig == 'N':
        if row + 2 < 8 and col - 1 >= 0:
            matrix[row + 2][col - 1] = '*'
        if row + 2 < 8 and col + 1 < 8:
            matrix[row + 2][col + 1] = '*'
        if row - 2 >= 0 and col - 1 >= 0:
            matrix[row - 2][col - 1] = '*'
        if row - 2 >= 0 and col + 1 < 8:
            matrix[row - 2][col + 1] = '*'
        if row + 1 < 8 and col - 2 >= 0:
            matrix[row + 1][col - 2] = '*'
        if row + 1 < 8 and col + 2 < 8:
            matrix[row + 1][col + 2] = '*'
        if row - 1 >= 0 and col - 2 >= 0:
            matrix[row - 1][col - 2] = '*'
        if row - 1 >= 0 and col + 2 < 8:
            matrix[row - 1][col + 2] = '*'

    return matrix

s = input().lower()

for row in chess_(s, 'N'):
    print(*row)