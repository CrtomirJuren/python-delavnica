"""
"""
import time
import logging
import random

# --- global constants ---
DEBUG = False

# --- global variables ---
# main application_flag
app_running = True
# game running
game_over = False
# who will win ?
winner = None
# who's turn is it
current_player = "X" # "O"
# game board   
board = []

def display_board():
    global board
    logging.debug('display_board()')

    print(board[0] +" | "+ board[1] + " | " + board[2]+ 5*" " + " 1 | 2 | 3 ")
    print(board[3] +" | "+ board[4] + " | " + board[5]+ 5*" " + " 4 | 5 | 6 ")
    print(board[6] +" | "+ board[7] + " | " + board[8]+ 5*" " + " 7 | 8 | 9 ")
    print("")

def check_game_over_condition():
    global game_over
    global winner

    logging.debug('check_if_game_over_condition()')

    win = check_win_condition()
    
    if win:
        winner = current_player
        logging.info(f'Player {winner} won game.')

    # if the game is won at the last cell,
    # dont check tie condition. or game will be win and tie    
    tie = check_tie_condition()
    # if no win and a tie, there is tie
    tie = tie and not win

    if tie:
        logging.info(f'Game is tied.')  

    if tie or win:
        game_over = True

def check_win_condition():
    global current_player
    global board

    # check rows
    row_win = check_rows(board,current_player)
    # check columns
    column_win = check_columns(board, current_player)  
    # check diagonals
    diagonal_win = check_diagonals(board, current_player)
    # win if any of conditions true
    win = (row_win or column_win or diagonal_win)

    # return result
    return win

def check_tie_condition():
    """ """
    global board

    logging.debug('check_tie_condition()')

    # is the board full and no wins
    empty_cells = board.count('-')
    logging.debug(f'Number of empty cells {empty_cells}')   

    tie = (empty_cells == 0)

    return tie

def check_rows(board, player):
    """ """
    logging.debug('check_rows()')
    win = False

    row_1 = board[0:3] # 1,2,3
    row_2 = board[3:6] # 4,5,6
    row_3 = board[6:9] # 7,8,9

    r_1_win = (row_1.count(player) == 3)
    r_2_win = (row_2.count(player) == 3)
    r_3_win = (row_3.count(player) == 3)

    win = (r_1_win or r_2_win or r_3_win)

    return win

def check_columns(board,player):
    """ """
    logging.debug('check_columns()')

    # stolpec je vsak element za tri indexe večji
    column_1 = board[0:9:3]
    column_2 = board[1:9:3]
    column_3 = board[2:9:3]
    
    # win if 3 in a column
    c_1_win = (column_1.count(player) == 3)
    c_2_win = (column_2.count(player) == 3)
    c_3_win = (column_3.count(player) == 3)

    win = (c_1_win or c_2_win or c_3_win)

    return win

def check_diagonals(board,player):
    """ """
    logging.debug('check_diagonals()')

    # --- DIAGONALE ---
    diagonal_1 = [board[0],board[4],board[8]] # 0 | 4 | 8
    diagonal_2 = [board[2],board[4],board[6]] # 0 | 4 | 8

    d_1_win = (diagonal_1.count(player) == 3)
    d_2_win = (diagonal_2.count(player) == 3)

    win = (d_1_win or d_2_win)

    return win
