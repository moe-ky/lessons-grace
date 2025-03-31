"""The Treasure Chest Challenge! 💰🔐
Challenge Description:

You have found a locked treasure chest! To open it, you need to enter the correct secret code (a 3-digit number). 
You have 3 attempts to guess the code correctly. If you guess right, you win the treasure! If you fail all attempts, the chest remains locked forever.

Skills Tested:
✅ Using variables
✅ Using input() to get user input
✅ Using conditionals (if/else)
✅ Using a loop to limit attempts
give the user a hint any of their numbers 
being present in the computer generated numbers
when they have given a wrong number

User Hint: home work - 2025-04-01
You need to let the user know how many numbers they have guess correctly 
e.g. if code is 234 and user guess is 435 it should let them know that they have guessed 2 numbers correctly (i.e. 3 and 4)
you will need an array / list to store all the correct guesses
and you will need to use the length of the array / list to let the user know how many numbers they guessed correctly
"""


import random
# code = str(random.randint(100, 999))  # generating a three digit code
code = str(456)  # generating a three digit code


def treasure_chest():
    print(f"Welcome to the treasure chest, where you guess to unlock the chest")
    attempts = 0
    while attempts < 3:
        guess = input("Enter your three digit guess here: ")
        if guess == code:
            print("Congratulations! You've unlocked the treasure!")
            break
        else:
            print("Wrong code. Try again.")
            attempts += 1
            for i in guess:
                if i in code:
                    print(i)
                    print(f"")

    print(f"You've used all your attempts. The chest will remain locked forever. The code was {
        code}.")


treasure_chest()
