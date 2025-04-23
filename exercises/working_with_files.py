# to read from a file we use r mode
# with open('./inventory.csv', 'r') as f:
#     items = f.readlines()

# to append to a file we use a mode
# with open('./inventory.csv', '+a') as f:
#     f.writelines('Orange, 400')

# to write to a file we use w mode
# with open('./inventory.csv', 'w') as f:
#     for item in []:
#         f.writelines(f'{item}')


def list_all_inventory_items(file_path):
    """
        return a list of all the items in the inventory
    """
    with open(file_path, 'r') as f:
        items = f.readlines()
    return items
    
def add_items_to_inventory(file_path, items_to_add):
    """
        this function adds items to the inventory file
    """
    with open(file_path, 'a') as f:
        f.writelines(items_to_add + '\n')

def run():
    
    inventory_file_path = "./inventory.csv"
    
    print("Hello Shop Owner")
    user_choice = input("what would you like to do today? ")
    
    if user_choice == 'view all items':
        items = list_all_inventory_items(inventory_file_path)
        if len(items) == 0:
            print("it looks like you have no items in the inventory")
        else:
            print(items)
            
    elif user_choice == "add new item":
        user_item_to_add = input("please provide item in the following format, Item, Price e.g. Apples, 300 ")
        add_items_to_inventory(inventory_file_path, user_item_to_add)

run()

      
  
# # update an item in the inventory
# new_items_list = []
# for item in items:
    
#     # update price
#     if 'Apple' in item:
#         new_items_list.append('Apple, 200')
            
#     # remove item
#     elif 'Orange' in item:
#         pass
    
#     else:
#         new_items_list.append(item)

# print(new_items_list)

