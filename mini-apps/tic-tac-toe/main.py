import tic_tac_toe_modul as ttt

# players
players = ['X','O']

# generiraj random board
board = ttt.generate_random_board()

# izpisi board
ttt.print_board(board)

for player in players:
    # preveri ali je kdo zmagal
    win = ttt.check_win(board, player)

    if win:
        print(f'player {player} won the game')

    if not win:
        ttt.check_tie(board)