"""
Description
Compute the total cost for a single line item (name, quantity). Ignore unknown items and quantities ≤ 0.

Learning goals
    Tuple unpacking
    Guard clauses
    Rounding to 2 decimal places with round(x, 2)

PRICE_LIST = {"apple": 0.80, "bread": 1.50, "milk": 1.15, "banana": 0.30}

assert line_total(PRICE_LIST, ("apple", 3)) == 2.40
assert line_total(PRICE_LIST, ("eggs", 2)) == 0.0
assert line_total(PRICE_LIST, ("milk", 0)) == 0.0

Plan:
create a function called line_total with parameters price_list and item
use an if statement to take care of unknown items and quantities
use key value pairs to access the price of item in the dictionary
cost = price * quantity
return cost in 2dp
"""

from const import PRICE_LIST
# please write the code below to get me the price of apple from the PRICE_LIST dictionary
# new_item = "bread"
# print(PRICE_LIST[new_item])
# print(PRICE_LIST.get(new_item))
# print(PRICE_LIST.get("apple"))
# print(PRICE_LIST["apple"])

from const import PRICE_LIST
def line_total(price_list, item):
    quantity_of_item = item[1] 
    produce = item[0]
    if quantity_of_item <= 0:
        pass
    if produce not in price_list:
        pass
    if produce in price_list:
        cost_of_item = price_list.get(produce)
        total_cost = cost_of_item * quantity_of_item
    return round(total_cost, 2)

print(line_total(PRICE_LIST, ("apple", 3)))
print(line_total(PRICE_LIST, ("eggs", 3)))
