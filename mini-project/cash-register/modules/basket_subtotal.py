"""
Description
Sum the totals for a whole basket (a list of (item, qty) tuples).

Learning goals
    - Loop/accumulation pattern
    - Compose functions (line_total within subtotal)
    - Handle empty inputs

Input/Output examples
subtotal(PRICE_LIST, [("apple", 2), ("bread", 1)]) -> 3.10
subtotal(PRICE_LIST, []) -> 0.0
subtotal(PRICE_LIST, [("banana", -1), ("eggs", 3)]) -> 0.0

def subtotal(price_list, basket):

Plan:
create a total variable called basket_total,
using a for loop to loop through the basket,
use an if statement to take care of cost calc
"""
from line_total import line_total
from const import PRICE_LIST
def subtotal(price_list, basket):
    basket_total = 0.0
    for item in basket:
        basket_total += line_total(price_list, item)
    # prices = [line_total(price_list, item) for item in basket]
    return basket_total
