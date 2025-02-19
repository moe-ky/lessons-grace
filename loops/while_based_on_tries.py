# Import the randint function from the random module to generate random numbers
from random import randint

# Initialize a counter variable to keep track of the number of times the game has been played
current_no_times = 1

# Set the maximum number of times (guesses) allowed in the game
max_no_times = 5

# Start a loop that runs as long as the current count is less than or equal to the maximum allowed
while current_no_times <= max_no_times:
    
    # Prompt the user to guess a number between 1 and 5
    ask_user = input("Guess the number in my hand (between 1 and 5)...: ")
    
    # Increase the counter by 1 each time the loop runs (each guess counts as one turn)
    current_no_times += 1
    
    # Generate a random number between 1 and 5 for this turn
    number = randint(1, 5)
    
    # Convert the user's guess from a string to an integer and compare it with the random number
    if int(ask_user) == number:
        print("Yay, you guessed it!")  # Message if the guess is correct
    else:
        print("Oops, try again!")  # Message if the guess is incorrect
