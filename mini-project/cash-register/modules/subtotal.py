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
