"""
EMI Calculator
You'll practice
Multiple inputs feeding a real-world formula
Ask the user for a loan amount, an annual interest rate (percent), and a tenure in months.
Compute the monthly EMI (equated monthly instalment).

Formula:

r = (annual_rate / 12) / 100          # monthly rate as a decimal
EMI = P * r * (1 + r)**n / ((1 + r)**n - 1)
where P is the loan amount and n is the number of months.

Print the EMI rounded to 2 decimal places.

Example:

Loan amount: 500000
Annual interest rate (%): 8.5
Tenure (months): 60
Monthly EMI: Rs 10258.27

"""

# Read inputs as floats — input() returns strings, so convert before math
P = float(input("Loan amount: "))
annual_rate = float(input("Annual interest rate (%): "))
n = int(input("Tenure (months): "))

# Monthly interest rate as a decimal
r = (annual_rate / 12) / 100

# EMI formula
EMI = P * r * (1 + r)**n / ((1 + r)**n - 1)

print(f"Monthly EMI: Rs {round(EMI, 2)}") # here we use round() which is a python built-in function

"""
In Python, round() is a built-in function used to round a floating-point number to a
specified number of decimal places.

Syntax is :

round(number, ndigits) 

where,

number: The value you want to round (in this case, your emi variable).

ndigits: The number of decimal places to round to (in this case, 2).


How this round() built-in function will works in my code:
If  raw calculated emi value is 10258.27493, then:
by
round(EMI, 2)
This evaluates to 10258.27.
"""