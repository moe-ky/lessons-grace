# Import the randint function from the random module to generate a random number
from random import randint

# This variable controls whether the game continues running
keep_playing = True

# Start a loop that will keep running until the player decides to exit
while keep_playing:
    
    # Ask the user to guess a number or type 'exit' to quit the game
    ask_user = input("Guess the number in my hand (between 1 and 5)... or type 'exit' to leave the game: ")

    # Check if the user wants to exit the game
    if ask_user.lower() == "exit":  # Using .lower() to handle cases where user types "EXIT" or "Exit"
        print("Okay, bye bye!")  # Farewell message
        keep_playing = False  # Stop the loop, ending the game

    else:
        # Generate a random number between 1 and 5
        number = randint(1, 5)
        
        # Convert the user's input to an integer and compare it with the random number
        if int(ask_user) == number:
            print("Yay! You guessed it!")  # If the guess is correct
        else:
            print(f"Oops, try again! The number was {number}")  # If the guess is incorrect, reveal the number
