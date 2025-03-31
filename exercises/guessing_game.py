"""
This is a guessing game
the computer will ask you if you want to play, until you have played 5 rounds
the computer will pick a random number
if you guess the number right, you get a point
at then end of the 5 rounds, print how many points you have
"""
# pseudocode
""" in this guessing game the computer will be able choose a number with the use of a random library
    and the user will have to guess the number with 5 chances at their disposal, using a while loop
    the user will be asked for their guess with use of an input statement and
    with the use of print statements, the user will be told they got the answers wrong
    and when they guess the number right they have a point and the point is counted"""

# computer has to generate a number between 1 to 10




import random  # the library the comp  # uter uses to generate a random number
def guessing_game():
    user_score = 0
    print("-" * 20)
    print("Welcome to the number guessing game \n")
    print("You have  five rounds \n")
    print("-" * 20)
    computer_num = random.randint(1, 10)

    game_rounds = 0  # there are five rounds in this game
    user_choice = input(
        "Do you want to play the guessing game? (yes/no): ")
    print(user_choice)
    while game_rounds < 5:  # while zero is not equal zero
        if user_choice.lower() == 'yes':  # if yes is not equal to yes, in this case i thought this means "no"
            print("Let's go")
            user_num = int(
                input("Between 1 and 10, select a number of your choice: "))
            print(user_num)
            if user_num == computer_num:
                print(f"You got the answer right")
                user_score += 1
            elif user_num > computer_num:
                print(f"Your guess {
                    user_num} is bigger than computer's guess, try again!")
            else:
                print(f"Your guess {
                    user_num} is lesser than computer's guess, try again!")
        else:
            print("Game not started. Exiting.")
            break
        game_rounds += 1
        print(computer_num)
        print(user_score)


guessing_game()
