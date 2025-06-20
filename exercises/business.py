revenue = [150.0, 200.5, 340.75]

# create a function that sums up the revenue number, do not use the sum function
def total_revenue():
    total = 0 
    for i in revenue:
        total = total + i
    return (total)
        
total_revenue()

# create a function called apply_discount
# it will take in two parameters price and discount
# example apply_discount(200, 50) -> 100 (new price after discount applied)
def apply_discount(price, discount):
    discounted_price = price * discount / 100
    print(discounted_price)

# apply_discount(200, 50)

# create a function called count_orders
# it will aggregate unique items, given a list of orders for those items
# example: count_orders(['A-001', 'A-002', 'A-001']) -> return a dictionary {A-001: 2, A-002: 1}

def count_orders(list_of_orders: list):
    aggregated_orders = {}    
    for order in list_of_orders:
        # we need logic here to check if order (which is the key), already exists in the dictionary:
        if order in aggregated_orders.keys():
            current_count = aggregated_orders[order] # e.g. aggregated_orders['A-001'] -> 1 (which will be 1 when we first see it)
            new_count = current_count + 1
            aggregated_orders[order] = new_count
            print(f"{order} has been seen before, updating count by 1, new order count is {new_count}")
        else:
            print(f"{order} has NOT been seen before, updating count by 1")
            aggregated_orders[order] = 1
        
    print(aggregated_orders)
    
count_orders(['A-001', 'A-002', 'A-001','A-001', 'A-002', 'A-003','A-001', 'A-002', 'A-004','A-001', 'A-009', 'A-001'])
