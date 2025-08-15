"""
1. Inventory Tracker
Scenario: You work at a small e-commerce startup. You're given a dictionary of product inventory and a list of orders. Your task is to update the inventory accordingly.

Skills Tested: Dictionaries, loops, conditional logic.
"""

inventory = {
    'Laptop': 10,
    'Mouse': 25,
    'Keyboard': 15,
    'Speakers': 2,
    'Chair': 10,
    'Table': 10,
    'Cables': 20,
}

orders = ['Laptop', 'Mouse', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Chair', 'Table', 'Cables']

for order in orders:
    print ("user has ordered one: ", order)
    # update the inventory
    inventory[order] -= 1
    # if order == "Laptop":
    #     inventory["Laptop"] -= 1
    # elif order == "Mouse":
    #     inventory["Mouse"] -= 1
    # else:
    #     inventory["Keyboard"] -= 1

print(inventory)

"""
2. Monthly Revenue Report
Scenario: You’re helping the finance department. You're given a list of daily sales and need to compute total revenue and average daily sales.

Skills Tested: Lists, basic math, built-in functions.

daily_sales = [1200, 1350, 1100, 980, 1430, 1600, 1500]

# TODO:
# 1. Calculate total revenue
# 2. Calculate average daily sales
"""
daily_sales = [1200, 1350, 1100, 980, 1430, 1600, 1500]
total = 0
for i in daily_sales:
    total += i
print(total)

n = len(daily_sales)
avg = total // n
print(avg)
