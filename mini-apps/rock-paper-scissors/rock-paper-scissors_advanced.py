import random

moves = ['rock','paper','scissors']

# functions
def game_start():
    print('****************************************')
    print('*  welcome to rock-paper-scissors game *')
    print('*  to exit game press ctrl+c           *')
    print('****************************************')
9
def game_play():
    print('\n0 = rock, 1 = paper, 2 = scissors')
    index = int(input("player select move: "))

    pc = random.choice(moves)
    player = moves[index]

    print(f'pc played = {pc}, player played = {player})')
    winner = None
    winner_type = None

    # NAPREJ PREVERI IZENAČENJE
    if player == pc:
        pass

    # POTEM PREVERI ZMAGO
    else:
        # rock > scissors, rock < paper
        if player == 'rock':
            if pc == 'scissors':
                winner_type = 'player'
                winner = player
            if pc == 'paper':
                winner_type = 'pc'
                winner = pc

        # paper > rock, paper < scissors
        if player == 'paper':
            if pc == 'scissors':
                winner = pc
                winner_type = 'pc'
            if pc == 'rock':
                winner = player
                winner_type = 'player'

        # scissors > paper, scissors < rock
        if player == 'scissors':
            if pc == 'paper':
                winner = player
                winner_type = 'player'
            if pc == 'rock':
                winner = pc
                winner_type = 'pc'

    if winner == None:
        print('It"s a tie.')
    else:
        print(f'Zmagal je {winner_type}. Igralo se je {player} proti {pc}.')

def game_exit():
    print('thank you from playing')

# application
def main():
    # play game
    game_start()

    while True:
        try:
            # play game
            game_play()

            # ask if continue playing
            user_input = int(input(f'\nSelect Play Again = 0, Exit = 1 : '))
            
            if user_input: # če je user input karkoli drugega kot 0, je konec zanke
                break
        
        # if ctrl+c is pressed, exit game
        except KeyboardInterrupt as e:
            print('\nuser exit')
            break

    game_exit()

# start application
main()