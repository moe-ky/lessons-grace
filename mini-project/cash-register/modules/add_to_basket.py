"""
Challenge 4 — Add to Basket (Merging Quantities)
Description: Write a helper that adds (name, qty) to a basket, merging with existing quantities for the same item. Ignore non-positive qty. 
Do not crash on unknown items; simply allow adding (pricing rules will ignore unknowns later).

Learning goals
    - Mutating lists safely
    - Searching within a list of tuples
    - Basic input validation

Function signature
def add_to_basket(basket: list[tuple[str, int]], name: str, qty: int) -> list[tuple[str, int]]:
    ...
    
Input/Output examples
add_to_basket([], "apple", 2) -> [("apple", 2)]
add_to_basket([("apple", 2)], "apple", 3) -> [("apple", 5)]
add_to_basket([("bread", 1)], "bread", 0) -> [("bread", 1)]

Acceptance criteria
    - Returns a new basket (do not mutate the original list)
    - If qty <= 0, return basket unchanged
    - Merge with existing item name (exact match)

Plan:
create a function called add_to_basket(basket, name, qty)
use a for loop to go through the basket 
use an if statement to ignore non positive quantities,
use the else statement to take care of adding the append function
using the append function to add the items of produce to the current amount in the basket

Plan:
create a function called add_to_basket(basket, name, qty)
create a new_basket variable and set it to an empty list (or create a copy of the basket)
take the name and qty parameters:
- if the qty is less than or equal to 0, return the basket unchanged
- if the name is already in the basket, merge with existing item name (exact match) and update the quantity. 
    then return the new_basket with the updated items.
- if the name is not in the basket, append the (name, qty) tuple to the new_basket
finally return the new_basket
"""

def add_to_basket(basket, name, qty):
    new_basket = list(basket)
    if qty <= 0:
        return basket
    
    if len(basket) == 0:
        new_basket.append((name, qty))
        return new_basket
    
    for item in basket:
        if name == item[0]:
            qty_in_basket = item[1]
            new_qty = qty_in_basket + qty
            new_item = (name, new_qty)
            new_basket.remove(item)
            new_basket.append(new_item)
        else:
            new_basket.append((name, qty))
    
    return new_basket
