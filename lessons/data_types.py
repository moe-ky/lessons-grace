# recommend reading from chapter 1 - 6 of the automate the boring stuff 

name = "Grace" # String
age = 20 # Int
weight_of_textbook = 12.4 # Float
favorite_things = [1, 2, 3, "animals", "fruits"] # List
pets = { "dog": "sparky", "cat": "lucile" } # Dictionary
secret_coordinates = (2,3) # Tuple => immutable list
has_a_dog = True # Boolean
has_a_hamster = False # Boolean


# STRING DATA TYPE
# string methods https://www.w3schools.com/python/python_ref_string.asp

print(name[0:3])
print(name.upper())
print(name.lower())
print(name.islower())

# LIST DATA TYPE
# list methods https://www.w3schools.com/python/python_ref_list.asp
favorite_things.append("goat_meat")
favorite_things.append("tennis")
favorite_things.append("concerts")
print(favorite_things)

for item in favorite_things:
    print("item is: ", item)
    
# DICTIONARY DATA TYPE
phonebook = {"ola": "09865", "jean": "043920"}
print(phonebook["ola"])
print(phonebook.get("ola"))

for name, number in phonebook.items():
    print(f"name is {name} and their number is {number}")

# TUPLE DATA TYPE
print(secret_coordinates[0])
