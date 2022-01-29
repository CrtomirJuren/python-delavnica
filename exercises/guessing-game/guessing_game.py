"""
GUESS A NUMBER GAME
- exercise while loop, if-else logic, game logic
- handle user inputs

Reactions to user input and game logic

version_1:
	'Completely out of range. Do you even understand the game?'
	'Too low, try again!'
	'Too high, try again!'
	'You guessed!'

version_2:
	'Press "y" to keep playing.'50
	'game over, thank you for playing!'

version_3:
- create application that checks if user input is number
	'I only accept integer numbers! Try again.'
"""

import numpy as np
import numbers

# our number limits
high_num = 100
low_num = 0
guessing_num = np.random.randint(low_num,high_num)
input_num = None

def get_user_input():

	try:
		x = int(input('Enter number: '))
	except:
		x = None
		print('I only accept integer numbers! Try again.')
	
	return x

def check_answer(x):
	#check input range
	if x < low_num or x > high_num:
		print('Completely out of range. Do you even understand the game?')
		return False	
		
	if x < guessing_num:
		print('Too low, try again!')
		return False

	if x > guessing_num:
		print('Too high, try again!')
		return False

	if x == guessing_num:
		print('You guessed!')

		if input('Press "y" to keep playing.') == 'y':
			print(f'Guess a number between {low_num} and {high_num}:')
			return False
		else:
			print('game over, thank you for playing!')
			return True

# start main game loop
print(f'Guess a number between {low_num} and {high_num}:')
# game_over = False

while True:

	user_input = get_user_input()
	
	if user_input != None:

		if check_answer(user_input):
			break








