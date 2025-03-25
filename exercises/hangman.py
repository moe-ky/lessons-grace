import random
words = ['apple', 'ball', 'cherry']
selected_word = random.choice(words)
print(f"hint: the selected word is {selected_word}.")

current_game_state = list('_' * len(selected_word))
display_string = " ".join(current_game_state)
    
no_tries = 1
while no_tries < 11 and display_string != selected_word:
    
    # get the user input
    user_input = input(f"here is the word {display_string}, what is your next guess? ")
    
    # find all the positions where the users guessed letter exists in the computers selected word
    present_index = []
    # check if the user input exists in the selected word
    if user_input in selected_word:
        # for each index and character in the selected word, save the index.
        for index, character in enumerate(selected_word): # -> research what the enumerate function allows you to do
            # example: r is in the 3rd position and 4th position for cherry - so we are saving 3 and 4 in out present_index list
            if character == user_input:
                present_index.append(index)
                
    print (f"present index after guess = {present_index}")
                
    for positions in present_index:
        print (f"replacing {current_game_state[positions]} with {user_input}")
        current_game_state[positions] = user_input

    display_string = "".join(current_game_state)
    no_tries += 1

if display_string == selected_word:
    print(f"congratulations you guessed the word {selected_word}")
