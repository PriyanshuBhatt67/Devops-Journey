"""
1. Type Conversion (Implicit)

Type conversion—specifically implicit type conversion—happens automatically. The Python 
interpreter changes one data type into another behind the scenes to avoid errors and prevent data loss.
• Example: Adding an integer to a float

"""
x = 10    # Integer
y = 5.5   # Float
z = x + y # z becomes 15.5 (Float) because when mixing values, python follows Hierarchy 
# And based on the Hierarchy,so here Python automatically converts x to 10.0 so it 
# can perform the mathematical operation seamlessly
print(z)

# and the hierarchy is Complex(complex)>Float(float)>Integer(int)>boolean(bool)

#When you perform an operation between two different types, Python automatically upcasts the
# lower type to match the higher type before executing the operation.

"""
2. Type Casting (Explicit)

Type casting—or explicit type conversion—happens manually. This is when you, the programmer, 
force an object to change into a specific data type using built-in functions (constructors)
like int(), float(), or str().
• Example: Turning user input (which always arrives as a string) into an integer.

"""
age_input = "25"         # String
age = int(age_input)     # Manually casting to an Integer
print(age)
#Unlike implicit conversion, manual type casting can result in data loss.
# For instance, casting int(5.99) will cut off the decimals and return 5 

a=5.7
b=int(a) # convert into integer 5 and storing into b variable
print(b) #printing present value of b now which is 5
print(type(b)) # int
