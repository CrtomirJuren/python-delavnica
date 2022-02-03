from random import choice

def generate_random_board():
    board = []
    vzorci = ['X','O']
    i = 0
    for x in range(3):
        row = []
        for y in range(3):
            # i += 1
            nakljucen_vzorec = choice(vzorci)
            row.append(nakljucen_vzorec)
        board.append(row)
    
    return board

def print_board(board):
    for row_index in range(3):
        print(board[row_index])