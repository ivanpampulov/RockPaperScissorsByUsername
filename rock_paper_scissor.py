#Read user input
import random

rock = 'Rock'
paper = 'Paper'
scissor = 'Scissor'

#colors
def prRed(skk): print('\033[91m {}\033[00m' .format(skk))
def prGreen(skk): print('\033[92m {}\033[00m' .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

#logic

player_move = input('Choose [r]ock, [p]aper, [s]cissor: ')

if player_move == 'r':
    player_move = rock

elif player_move == 'p':
    player_move = paper

elif player_move == 's':
    player_move = scissor

else:
    raise SystemExit('Invalid Input. Try again ...')

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock

elif computer_random_number == 2:
    computer_move = paper

elif computer_random_number == 3:
    computer_move = scissor

print(f'You chose {player_move}')
print(f'The computer chose {computer_move}')

if (computer_move == rock and player_move == paper) or (computer_move == paper and player_move == scissor) or \
        (computer_move == scissor and player_move == rock):
    prGreen('Congratulations! You win!')

elif computer_move == player_move:
    prYellow('It\'s a draw. Try again!')

else:
    prRed('You lost! Try again.')