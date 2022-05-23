""" funkcije uporabljene v tic tac toe igri """
import random

igralca = ['X','O']

def generate_random_board():
    """ funkcija ki generira naključno igralno ploščo"""
    board = []
    for j in range(3):
        
        # --- koda za generiranje vrstice
        vrstica = []
        for i in range(3):
            igralec = random.choice(igralca)
            vrstica.append(igralec)

        # pripni vrstico v board
        board.append(vrstica)

    return board

def print_board(board):
    """ nariše board v terminal """

    for vrstica in board:
        print(vrstica)

def check_win(board, player):
    print('------------')
    print(f'checking player {player}')

    win_row = check_row_win(board, player)
    win_column = check_column_win(board, player)
    win_diagonal = check_diagonal_win(board, player)

    win = win_row or win_column or win_diagonal

    # presledek
    print('------------')

    return win

def check_row_win(board, player):
    print('checking row win')
    row_1 = board[0]
    row_2 = board[1]
    row_3 = board[2]

    row_1_win = (row_1.count(player) == 3)
    row_2_win = (row_2.count(player) == 3)
    row_3_win = (row_3.count(player) == 3)

    win = row_1_win or row_2_win or row_3_win
    
    if row_1_win:
        print('win on row 1')
    elif row_2_win:
        print('win on row 2')
    elif row_3_win:
        print('win on row 3')
    else:
        pass

    return win

def check_column_win(board, player):
    """
    [['O', 'X', 'O'],
     ['O', 'X', 'O'],
     ['X', 'X', 'X']]
    """
    print('checking column win')
    column_1 = [board[0][0], board[1][0], board[2][0]]
    column_2 = [board[0][1], board[1][1], board[2][1]]
    column_3 = [board[0][2], board[1][2], board[2][2]]

    column_1_win = (column_1.count(player) == 3)
    column_2_win = (column_2.count(player) == 3)
    column_3_win = (column_3.count(player) == 3)

    win = column_1_win or column_2_win or column_3_win
    
    if column_1_win:
        print('win on column 1')
    elif column_2_win:
        print('win on column 2')
    elif column_3_win:
        print('win on column 3')
    else:
        pass  

def check_diagonal_win(board, player):
    print('checking diagonal win')
    """
    [['O', 'X', 'O'],
     ['O', 'X', 'O'],
     ['X', 'X', 'X']]
    """
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]

    diagonal_1_win = (diagonal_1.count(player) == 3)
    diagonal_2_win = (diagonal_2.count(player) == 3)

    win = diagonal_1_win or diagonal_2_win
    
    if diagonal_1_win:
        print('win on diagonal 1')
    elif diagonal_2_win:
        print('win on diagonal 2')
    else:
        pass  

def check_tie(board):
    """
    [['O', '-', 'O'],
     ['O', 'X', '-'],
     ['-', 'X', 'X']]
    """
    empty_cells = board.count('-')
    tie = (empty_cells == 0)

    return tie