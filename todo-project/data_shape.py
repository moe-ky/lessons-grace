to_do_list = {
    "1": "go to the market",
    "2": "buy groceries"
}

status_update = {
    "1" : "completed",
    "2" : "incompleted"
}

# show me how you are going to list the todo items and their status
# example output:
# 1: go to the market (completed)

#plan - list all the items in the to do list
#check status of action (i.e. completed or incompleted)
#update the status in the for loop
#nested loop is needed

# for id, desc in to_do_list.items():
#     status = status_update.get(id)
#     print(id, desc, status)
    
description = to_do_list.get("1")
updated_description = f"{description} (completed)"

print(f"Description of item 1: {description}")
print(f"Updated description of item 1: {updated_description}")
