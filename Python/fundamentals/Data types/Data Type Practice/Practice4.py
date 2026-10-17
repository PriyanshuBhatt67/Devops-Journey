#4. Take two numbers from input() and calculate their sum.

# so we have to take 2 numbers as input and calculate their sum

Num1=input("Enter First Number : ")
Num2=input("Enter Second Number : ")

 # Now Converting Both Num into Integers
Num1_Int=int(Num1) # Num1 lai integer maa convert gardae
Num2_INt=int(Num2) # Num2 lai integer maa convert gardae

#sum calculate gardae
sum= Num1_Int + Num2_INt
#sum lai print gardae
print(sum)

# OR yesto ni garna sakinxa

# Take two numbers from the user
# float() allows the program to accept both whole numbers and decimals
num1 = float(input("Enter the First number : "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
result = num1 + num2 # python ko dynamic typing feature le garda when we add both 
#float values and put into another variable and another variable ko DataType ni Float

# Display the result
print(f"The sum of {num1} and {num2} is {result}")
