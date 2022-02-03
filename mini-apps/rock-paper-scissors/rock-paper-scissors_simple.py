""" 
Paper Rock Scissors

RULES
    papir < škarje
    kamen < papir
    škarje < kamen

    če sta oba ista.. potem je izenačeno

HINT:
if player == 'rock' and ai =='paper':
    print('ai wins')
"""
import random

moves = ['rock','paper','scissors']

pc = random.choice(moves)

print('0 = rock, 1 = paper, 2 = scissors')
index = int(input("select move: "))
player = moves[index]

print(f'pc = {pc}, player = {player})')

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
