import sys
import json

# an item in the todo list will contain an id, a description of the task

with open('todo.json', 'r') as file:
    todo_item = json.load(file)
    print(f"Loaded todo items: {todo_item}")
    
    
def save_todo_items(todo_dict):
    """
    Save the todo items to a JSON file.
    """
    with open('todo.json', 'w') as file:
        json.dump(todo_dict, file, indent=4)

"""
task: add a new item to the todo list
id: 1
description: Buy groceries    
"""
# todo_item[1] = 'buy groceries'
# todo_item.update({2: 'clean the house'})

"""
task: create a function to add a new item to the todo list
function name: add_todo_item
parameters: todo_dict, item_id, description
    - todo_dict: the dictionary containing todo items
    - item_id: the id of the new todo item
    - description: the description of the new todo item
example usage: add_todo_item(todo_item, 3, 'walk the dog')
result: todo_item = {1: 'buy groceries', 2: 'clean the house', 3: 'walk the dog'}
whats happened: a new item with id 3 and description 'walk the dog' was added to the todo_item dictionary
"""

"""
task: update the add_todo_item to automatically create a new item with a unique id
function name: add_todo_item
parameters: todo_dict, description
    - todo_dict: the dictionary containing todo items
    - description: the description of the new todo item
example usage: add_todo_item(todo_item, 'walk the dog')
result: todo_item = {1: 'buy groceries', 2: 'clean the house', 3: 'walk the dog'}
whats happened: the function generates a new id based on the current length of the todo_dict and adds the new item with that id
"""

def add_todo_item(todo_dict, description):
    """
    Task Plan:
    create a variable called length_of_dict to hold the current length of the todo_dict
    generate a new id, store in a variable called new_id - this will be the length_of_dict + 1
    add the item to the todo_dict with the new_id and description
    """
    length_of_dict = len(todo_dict)
    new_id = length_of_dict + 1
    todo_dict.update({new_id: description})
    save_todo_items(todo_dict)

# add_todo_item(todo_item, 3, 'walk the dog')

"""
task: create a function to list all todo items
function name: list_todo_items
parameters: todo_dict
    - todo_dict: the dictionary containing todo items
example usage: list_todo_items(todo_item)
result: prints all todo items in the format "id: description"
    1: buy groceries
    2: clean the house
    3: walk the dog
whats happened: the function iterates through the todo_dict and prints each item in the specified format
"""

def list_todo_items(todo_dict):
    # for item in todo_dict.items():
    #     print(f'{item[0]}: {item[1]}')
    
    print("Todo List:")
    for id, desc in todo_dict.items():
        print(f'{id}: {desc}')

# list_todo_items(todo_item)
    
"""
task: create a function to delete an item from the todo list
function name: delete_todo_item
parameters: todo_dict, item_id
    - todo_dict: the dictionary containing todo items
    - item_id: the id of the todo item to delete
example usage: delete_todo_item(todo_item, 2)
result: todo_item = {1: 'buy groceries', 3: 'walk the dog'}
whats happened: the function deletes the item with the specified id from the todo_item dictionary
"""
def delete_todo_item(todo_dict, item_id):
    print(f"Deleting item with id: {item_id}")
    del todo_dict[item_id]
    save_todo_items(todo_dict)
    
# delete_todo_item(todo_item, 2)
# list_todo_items(todo_item)

"""
task: create a function to mark a todo item as completed
function name: complete_todo_item
parameters: todo_dict, item_id
    - todo_dict: the dictionary containing todo items
    - item_id: the id of the todo item to mark as completed
example usage: complete_todo_item(todo_item, 1)
result: todo_item = {1: 'buy groceries (completed)', 3: 'walk the dog'}
whats happened: the function updates the description of the specified item to indicate it is completed
"""
def complete_todo_item(todo_dict, item_id):
    retrieved_action = todo_dict.get(item_id)
    retrieved_action_update = f"{retrieved_action} (completed)"
    todo_dict.update({item_id: retrieved_action_update })

# complete_todo_item(todo_item, 1)
# list_todo_items(todo_item)

# fetch the action and details from command line arguments passed to the script
action = sys.argv[1] if len(sys.argv) > 1 else None
details = sys.argv[2] if len(sys.argv) > 2 else None
print(f"Action: {action}, Details: {details}")

"""
task: create some logic to handle the add action from the command line
if action is 'add', call the add_todo_item function with the details provided
example usage: python todo.py add 4 'read a book'
result: todo_item = {1: 'buy groceries', 2: 'clean the house', 3: 'walk the dog'}
whats happened: the script checks if the action is 'add', and if so, it calls the add_todo_item function with the provided details
"""
if action == 'add':
    add_todo_item(todo_item, details)
    list_todo_items(todo_item)

"""
task: create some logic to handle when the user want to delete an item
if action is 'delete', call the delete_todo_item function with the item_id provided
example usage: python todo.py delete 2
result: todo_item = {1: 'buy groceries', 3: 'walk the dog'}
whats happened: the script checks if the action is 'delete', and if so, it calls the delete_todo_item function with the provided item_id
"""
if action == 'delete':
    delete_todo_item(todo_item, details)
    list_todo_items(todo_item)

