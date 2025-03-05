# REQ 1: ask the user for their input, rock, paper or scissors
# REQ 2: the system should randomly pick an option between rock, paper or scissor (hint: research random.choice)
# REQ 3: apply the rules of the game, if the user and system picks the same item - then its a draw
# REQ 4: Let the user know if they won, lost or drew and what the computer selected

"""
    Rules of the game:
    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock
    potential user and computer picks = Rock, paper or scissors
    user - Rock, Computer - Rock = (a draw)
    user - Rock, computer - scissors = (User won)
    user - rock, computer - paper = (computer won)
    user - paper, computer - scissors = (computer won)
    user - scissors, computer - paper = (user won)
    user - paper, computer - rock = (user won)
    user - scissors, computer - rock = (computer won)

"""

# import random
import random
# ask the user for input
user_input = input(
    "Select a choice out of this three (Rock, Paper, Scissors).")
options = ['Rock', 'Paper', 'Scissors']
computer_option = random.choice(options)
print(computer_option)

if user_input == 'Rock' and computer_option == 'Scissors':
    print('user won')
elif user_input == 'Scissors' and computer_option == 'Paper':
    print('User won')
elif user_input == 'Paper' and computer_option == 'Scissors':
    print('Computer won')
elif user_input == 'Paper' and computer_option == 'Rock':
    print('User won')
elif user_input == 'Rock' and computer_option == 'Paper':
    print('Computer won')
elif user_input == 'Scissors' and computer_option == 'Rock':
    print('Computer won')
elif user_input == 'Paper' and computer_option == 'Scissors':
    print('Computer won')
else:
    print('A draw')
