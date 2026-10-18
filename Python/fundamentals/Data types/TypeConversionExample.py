"""
Temperature Converter You'll practice Reading input and converting strings to numbers Ask the user
 for a temperature in Celsius, then print it in both Fahrenheit and Kelvin. Formulas:
      • Fahrenheit = (C * 9/5) + 32 • Kelvin = C + 273.15 Remember: input() gives you a string,
so convert it with float() before doing any math — otherwise you'll hit the classic type error. 
Example: Enter temperature in Celsius: 37 37.0 C = 98.6 F 37.0 C = 310.15 K

"""
# Ask the user for input
celsius_str = input("Enter temperature in Celsius: ")

# Convert the input string to a decimal number (float)
celsius = float(celsius_str)

# Calculate the conversions using the formulas
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# Print the results
print(f"{celsius} C = {fahrenheit} F")
print(f"{celsius} C = {kelvin} K")

# OR we can do this as well

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius} C = {fahrenheit} F")
print(f"{celsius} C = {kelvin} K")