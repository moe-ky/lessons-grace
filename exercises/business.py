revenue = [150.0, 200.5, 340.75]

# create a function that sums up the revenue number, do not use the sum function
def total_revenue():
    total = 0 
    for i in revenue:
        total = total + i
    print(total)
        
total_revenue()
