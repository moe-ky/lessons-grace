yearly_salary = float(input("yearly_salary: "))
portion_saved = float(input("portion_saved: "))
cost_of_dream_home = float(input("cost_of_dream_home: "))
portion_down_payment = 0.25
amount_saved = 0
r = 0.05

down_payment = cost_of_dream_home * portion_down_payment
print("down payment required for dream home is", down_payment)

months = 0
while amount_saved <= down_payment:
    
    months += 1
    
    saved = portion_saved * (yearly_salary/12)    
    interest = (r/12) * amount_saved
    
    amount_saved += (saved + interest)
    print(f"in month {months}, you saved {saved}, gained {interest} in interest, for a total value of {amount_saved}")
    
print(months)
