import random
print("#"*100)
print("#"*25, "WELCOME TO THE ROCK, PAPER, SCISSORS GAME !!!")
print("#"*100)

def rps_logic(user_input, computer_option):
    if user_input == 'Rock' and computer_option == 'Scissors':
        return('User won')
    elif user_input == 'Scissors' and computer_option == 'Paper':
        return('User won')
    elif user_input == 'Paper' and computer_option == 'Scissors':
        return('Computer won')
    elif user_input == 'Paper' and computer_option == 'Rock':
        return('User won')
    elif user_input == 'Rock' and computer_option == 'Paper':
        return('Computer won')
    elif user_input == 'Scissors' and computer_option == 'Rock':
        return('Computer won')
    elif user_input == 'Paper' and computer_option == 'Scissors':
        return('Computer won')
    else:
        return('A draw')
    

# current challenge is to add a score counter
# by the end of the game, print out how many rounds the computer won, VS how many rounds the user won.
# output example is: GAME OVER - computer won {3} rounds, and user won {4} rounds

round_question = input("Do you want to play a round of RPS? 'Y' or 'N' ")

score_user = 0
score_computer = 0

while round_question == "Y":

    
    print(f"you have selected {round_question}, You can play the game")
    user_input = input("Select a choice out of this three (Rock, Paper, Scissors). ")
    computer_option = random.choice(['Rock', 'Paper', 'Scissors'])
    
    print(f"user selected {user_input}, and computer selected {computer_option}")
    result = rps_logic(user_input, computer_option)
    print ("result of this round is ", result)
    
    if result == 'User won':
        score_user += 1
    elif result == 'Computer won':
        score_computer += 1
    else:
        score_user += 1
        score_computer += 1
        
    round_question = input("Do you want to play another round of RPS? 'Y' or 'N' ")
    
print(f"GAME OVER - computer won {score_computer} rounds, and user won {score_user} rounds")


