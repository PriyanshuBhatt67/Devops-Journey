"""
Challenge 11: Storing values in variables and reusing them

Task: Build a simple interest calculator driven by variables.
Define three variables: principal, rate (percent per year), and time (in years). 
Then calculate:
- Simple Interest: (principal * rate * time) / 100
- Total amount: principal + SI

"""

#Pseudo Code(a step-by-step, informal description of a computer program or algorithm written in plain, human-readable language) :

"""
in Step 1: At first Defining the input variables required for this program
SET the     principal = 1000
SET the     rate = 5
SET the   time = 2

in Step 2: Calculate Simple Interest and Total Amount
Computing this     simple_interest = (principal * rate * time) / 100
Computing this           total_amount = principal + simple_interest

 IN Step 3 we  Display the results with labels
PRINT "Simple Interest:", simple_interest
PRINT "Total Amount:", total_amount 

"""
#My Solution is 

# Define the variables at the top (change these values to test!)
principal = 1000
rate = 5        # percent per year
time = 2        # in years

# Calculations
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

# Print results with clear labels
print(f"For a principal of ${principal}, {rate}% rate, and {time} years:")
print(f"Simple Interest : {simple_interest}")
print(f"Total Amount    : {total_amount}")