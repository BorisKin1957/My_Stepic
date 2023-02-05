'''Ходы ферзя

На шахматной доске стоит ферзь. Программa отмечает положение ферзя на доске и все клетки, которые бьет ферзь.
Клетку, где стоит ферзь, отмечена английской буквой Q, клетки, которые бьет ферзь, отмечены символами *,
остальные клетки заполните точками.
На вход программе подаются координаты ферзя в шахматной нотации (то есть в виде e4)'''



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


    if fig == 'Q':
        for j in range(8):
            matrix[row][j] = '*'
        for i in range(8):
            matrix[i][col] = '*'
        for i in range(8):
            for j in range(8):
                if i + j == row + col:
                    matrix[i][j] = '*'
        for i in range(8):
            for j in range(8):
                if i - j == row - col:
                    matrix[i][j] = '*'
        if row + 1 < 8 and col - 1 >= 0:
            matrix[row + 1][col - 1] = '*'
        if row + 1 < 8 and col + 1 < 8:
            matrix[row + 1][col + 1] = '*'
        if row - 1 >= 0 and col - 1 >= 0:
            matrix[row - 1][col - 1] = '*'
        if row - 1 >= 0 and col + 1 < 8:
            matrix[row - 1][col + 1] = '*'

    matrix[row][col] = fig

    return matrix


s = input().lower()

for row in chess_(s, 'Q'):
    print(*row)