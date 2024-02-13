table = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

def printStateOfTable():
    print('-------------')
    for row in table:
        cells = '| '
        for cell in row:
            cells += cell
            cells += ' | '
        print(cells)
        print('-------------')


printStateOfTable()