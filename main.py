table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def printStateOfTable():
    print('-------------')
    for row in table:
        cells = '| '
        for cell in row:
            cells += cell
            cells += ' | '
        print(cells)
        print('-------------')

def markCell(row, column, marker):
    print('hello')
    table[row][column] = marker

printStateOfTable()
markCell(1, 2, 'x')
printStateOfTable()