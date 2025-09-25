"""
Challenge 5 — Percentage Discount
Description

Apply a percentage discount to a subtotal. Percent is between 0 and 100. Round to 2 dp.

Learning goals

Defensive programming
 - Simple arithmetic with floats
 - Rounding/formatting

Function signature
def apply_percentage_discount(subtotal_value: float, percent_off: float) -> float:
    ...
    
Examples:
apply_percentage_discount(10.00, 10) -> 9.0
apply_percentage_discount(10.00, 0) -> 10.0
apply_percentage_discount(10.00, 150) -> 0.0

Acceptance criteria
- Percent < 0 → treat as 0
- Percent > 100 → treat as 100
- Return rounded to 2 dp
- Does not return negative totals

Plan:
create function that takes in parameters subtotal_value and percent_off
create a variable called percent
use an input statement to ask what amount of percent they want to give
use an if statement to make any percent less than 0, 0 and also do the same for negative nums
and elif any above 100, 100
# in the else block calculate percentage

"""
import subtotal
percent = percent_off /100
def apply_percentage_discount(subtotal, percent_off):
    if percent_off <=0:
       return 0.00
    elif percent_off => 100:
        return 100.00
   else:
        discount = subtotal * percent
        discounted_amout = subtotal - discount 
        return(round(discounted_amount)2)
 
