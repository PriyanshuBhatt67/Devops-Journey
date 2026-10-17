""" 
Data Types classifies the variable's value

OR

Python data types classify the type of value a variable holds, determining what operations can be
performed on it. Python is dynamically typed, meaning you do not need to explicitly
declare a type; the language infers it automatically upon assignment

OR
Data types in Python define the type of value stored in a variable and determine the operations 
that can be performed on that data. Since Python treats everything as an object, each value is
 associated with a specific data type.

i)Helps the interpreter understand how to store and process different kinds of data efficiently.
ii)Enables correct operations by ensuring only valid actions are performed on compatible data types.


Python Data Types are 
1) Numeric 
- Numeric Data Type is also classified into three types as
i) Integer # example is a=1
ii)float #example a=3.43
iii)Complex - complex numbers jun college maa padheko wala which is in the form a+ib and in 
number form as example 1+2i


3)Boolean -  The Boolean data type in Python (represented by the bool class) 
holds exactly one of two built-in values: True or False.

One example in Boolean is:

is_running = True
debug = False
is_healthy = cpu_usage < 80

print(type(is_running))     #This will print <class 'bool'>

As we know that we can evaluate any Python value or expression to see if it resolves to True or
 False using the built-in bool() function.
 Lets also know about Falsy Values and Truthy Values.

 In Python, the following values inherently evaluate to False:
• The keyword False
• None (representing the absence of a value)
• Numeric zero values: 0, 0.0, 0j # jastae print(type(0)) garda false value show hunxa and so on
• Any empty sequence or collection: "" (string),  [] (list),  () (tuple), {} (dictionary),   set()

Almost everything else evaluates to True:
• Any non-empty string, list, tuple, or dictionary
• Any non-zero number (positive or negative)

4)Set
-
i)set # Unordered collection of unique items ; example is {1, 2, 3}
ii)frozenset # immutable version of set ; example is frozenset([1, 2])

5) Sequence Type
- Sequence type is divided into 3 categories as
i)String
ii)List

iii)Tuple
iv)Range

6)Binary Type
i) bytes - Immutable byte data.  Examples is b"Hello"
ii) bytearray - Mutable array of bytes . Example is bytearray(5)



"""
Priyanshu=1
print(type(Priyanshu)) # This will show variable's data type  as integer

print(bool("Hello"))  # Returns True
print(bool(0))        # Returns False

A=3.34
print(type(A)) # Float will show

B=2+8j
print(type(B)) #Complex data type

C=True
print(type(C)) # Bool will be print 

"""
2)Dictionary(comes under Mapping Category)- a built-in data structure used to
 store data in key-value pairs.
 While Creating a Dictionary
We define a dictionary using curly braces {}, separating keys and values with a colon : """

# A dictionary representing a user profile
user = {
    "username": "coder123",
    "followers": 2500,
    "is_active": True,
    "languages": ["Python", "JavaScript"]
}

"""And While Accessing These Values in Dictionary

We look up a value by placing its key inside square brackets [], or by using
 the .get() method (which won't crash your code if the key doesn't exist) like """

 # Using square brackets
print(user["username"])  # Output: coder123

# Using the .get() method safely
print(user.get("followers"))  # Output: 2500
print(user.get("age", "Not Found"))  # Output: Not Found

"""
3. Adding and Modifying Items in Dictionary

To add a new pair or change an existing one, use the assignment operator (=) with the key.
"""
# Modifying an existing value
user["followers"] = 2501 

# Adding a new key-value pair
user["country"] = "Canada"

"""
4. Removing Items in Dictionary

You can remove items using the del keyword or the .pop() method.

"""
# Removes the "is_active" key and returns its value
user.pop("is_active") 

# Permanently deletes the "country" key
del user["country"] 

"""
5. Iterating Through a Dictionary

You can loop through a dictionary to access keys, values, or both simultaneously using .items()
"""
capitals = {"USA": "Washington DC", "India": "New Delhi", "France": "Paris"}

# Loop through both keys and values
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")


"""
4) set is a built-in data type used to store collections of unique, unordered items. They are highly 
efficient for removing duplicates and performing mathematical set operations like unions and 
intersections.

 Key Characteristics of Sets-
• Unique Elements: Duplicate values are automatically removed.
• Unordered: Items have no fixed position; we cannot access them via an 
index (e.g., my_set[0] will throw an error).
• Mutable Structure: You can add or remove items after the set is created.
• Immutable Items: The individual elements inside a set must be immutable
 (e.g., strings, numbers, tuples). we cannot put lists or dictionaries inside a set.

 Common Operations & Examples

1. Creating a Set

You can create a set using curly braces {} or the set() constructor.
 Note: To create an empty set, we must use set(). Empty curly 
braces {} will create an empty dictionary.
"""
# Creating a set with elements
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  
# Output: {'banana', 'apple', 'cherry'} (Duplicates are removed, order varies)

# Creating an empty set
empty_set = set()

"""
2. Modifying Elements in Set

Use .add() to insert a single item and .remove() or .discard() to delete an item.
"""
Numbers = {1, 2, 3}

# Add an element
Numbers.add(4) # {1, 2, 3, 4}

# Remove an element
Numbers.remove(2) # {1, 3, 4} (Throws an error if item doesn't exist)
Numbers.discard(9) # Works like remove, but safely ignores missing items


"""
3. Mathematical Set Operations

Python sets support native operations using either methods or special operators.

"""
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)          # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a.intersection(set_b)) # Output: {3}

#Difference of sets
print(set_a - set_b) # Output : {1,2}





# 7)None   DataType
# NoneType - Represents the absence of a value . 

#Beautiful useful example of None Type is 

# 1. Assigning None to a variable as a placeholder
user_email = None

# 2. Checking the data type of None
print(type(user_email))  
# Output: <class 'NoneType'>

# 3. Checking for None using the recommended 'is' operator
if user_email is None:
    print("No email address provided yet.")
else:
    print(f"User email is: {user_email}")

# 4. Updating the variable later with actual data
user_email = "alex@example.com"