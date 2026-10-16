"""Unpacking in Python allows you to assign elements of an iterable 
(like a list or a tuple) to multiple variables in a single line of code.
 The exact same syntax applies whether you are working with a list or a tuple.
Here we can see how we  use unpacking in various scenarios:"""
#1. Basic Unpacking means
#To unpack an iterable, place the variables on the left side of the assignment operator, 
# matching the exact number of elements inside the list or tuple on the right


# Unpacking a tuple

coordinates = (4, 5)
x, y = coordinates
print(x, y)  # Output: 4 5

# Unpacking a list
fruits = ["apple", "banana", "cherry"]
green, yellow, red = fruits
print(green, yellow, red)  # Output: apple banana cherry

#Note: If the number of variables does not match the number of items exactly, 
# Python will raise a ValueError.


#2. Extended Unpacking using *
#If we do not know the exact length of the list or tuple, OR    
# we only care about certain elements, use the asterisk operator (*) to collect the remaining values 
# into a new list

# Grabbing the first element and grouping the rest
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

# Grabbing the first and last elements
items = ("laptop", "mouse", "keyboard", "monitor")
first, *middle, last = items
print(first)   # Output: laptop
print(middle)  # Output: ['mouse', 'keyboard']
print(last)    # Output: monitor


#3. Unpacking in for Loops:
#A highly common and Pythonic way to use unpacking is directly inside a loop, 
# such as iterating over a list of tuples

# A list containing data packages as tuples
student_data = [("Alice", 22), ("Bob", 25), ("Charlie", 21)]

# Unpacking happens implicitly inside the loop declaration
for name, age in student_data:
    print(f"Student: {name}, Age: {age}")


 #4. Function Argument Unpacking
#You can also use the * operator to unpack a list or tuple directly into the 
# parameters of a function call

def multiply(a, b, c):
    return a * b * b

factors = [2, 3, 4]
# Unpacks the list items into variables a, b, and c
result = multiply(*factors) 
print(result)  # Output: 18
