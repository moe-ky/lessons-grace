"""
Description
    Write a function to safely look up the price of an item by name in a price list dictionary.
    Learning goals
    Read from a dictionary
    Return a default when a key is missing
    Write a pure function
    
Input/Output examples
    lookup_price(PRICE_LIST, "apple") -> 0.80
    lookup_price(PRICE_LIST, "eggs") -> None
    lookup_price({}, "apple") -> None    
        
Plan: 
use an if statement to check if item currently is in the price list,
if it does exist, return the cost of item,
if it doesn't return 'none'

"""
PRICE_LIST = {"apple": 0.80, "bread": 1.50, "milk": 1.15, "banana": 0.30}

def lookup_price(price_list=PRICE_LIST, item=""):
    return price_list.get(item, None)

print(lookup_price(PRICE_LIST, "apple")) # -> 0.80
