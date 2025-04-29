def add_name_to_file(name_to_find):
    """
        This adds a name to a file
    """
    # access the file in append mode
    output_file = open('names.txt', 'a')
    # append the name_to_find value into the file
    output_file.writelines(f'{name_to_find}\n')
    
def list_all_the_names():
    """
        List the names of everyone in the file.
    """    
    file_data = open('names.txt', 'r')
    for name in file_data:
        print(name)
        
def find_name_in_file(name_to_find):
    """
        Finds a name in the file and prints it, if it exists
    """
    
    file_data = open("names.txt", "r")
    for name in file_data:
        if name.strip() == name_to_find:
            print(f"yes, {name_to_find} exists in the file.")
            return # early return - which simply means as soon as you've gotten a certain result you exit the code early.
    
    print(f"sorry {name_to_find} does not exist in the file.")        
        
# add_name_to_file("Grace")
# add_name_to_file("Moe")
# add_name_to_file("Sam")
# list_all_the_names()
find_name_in_file("Sam")
find_name_in_file("Jules")
