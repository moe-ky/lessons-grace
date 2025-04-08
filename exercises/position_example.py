comp_guess = '123'
user_guess = '123'

# get the value of each character in the comp guess and their position
# pos 0 : value 1, pos 1: value 2, pos 2 is value 3
# do the same for user guess
# pos 0 : value 3, pos 1: value 2, pos 2 is value 1
# compare each matching position and their corresponding value
# pos 0 val 1 compared to pos 0 val 3 = no match, so wrong position
# pos 1 val 2 compared to pos 1 val 2 = match, so right position
# pos 2 val 3 compared to pos 2 val 1 = no match, so wrong position

comp_dict = {}
user_dict = {}

for index, value in enumerate(comp_guess):
    comp_dict[index] = value # {} add a key of index e.g. 0 with the value e.g. 1
    
for index, value in enumerate(user_guess):
    user_dict[index] = value # {} add a key of index e.g. 0 with the value e.g. 1
    
print(comp_dict)
print(user_dict)

all_required_positions = list(comp_dict.keys())
print(all_required_positions)
    
for pos in all_required_positions: # first value will be pos 0
    if comp_dict[pos] == user_dict[pos]:
        print(f"you have entered the correct number in the correct position - number is {user_dict[pos]} and position is {pos+1}")
    else:
        print(f"you have entered the number in the wrong position - number is {user_dict[pos]} and position is {pos+1}")
