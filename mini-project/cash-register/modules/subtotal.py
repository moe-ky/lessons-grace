"""
implement subtotal(price_list, basket) where:

    price_list is a dict like {"apple": 0.80, "bread": 1.50}
    basket is a list of (name, quantity) tuples
    ignore unknown items (don’t crash)
    ignore items with quantity <= 0
    return a float rounded to 2dp

acceptance criteria
    empty basket → 0.0
    unknown items are skipped silently
    correct total, rounding to 2 decimals
"""

def subtotal(price_list, basket):
    total = 0.0
    for item in basket:
        name_of_item = item[0]
        quantity_of_item = item[1]
        if quantity_of_item <= 0:
            print("ignoring items with 0 value")
        else:    
            if name_of_item in price_list:
                total += price_list[name_of_item] * quantity_of_item   
            else:
                print(f"unknown item '{name_of_item}' ignored")
    return round(total, 2)
