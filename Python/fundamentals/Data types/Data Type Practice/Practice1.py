# 1.Create one variable for each major built-in data type and print its type.

a=1
print(type(a)) #integer

b=1.2
print(type(b)) #float

c="priyanshu"
print(type(c)) #str/string

d=True
print(type(d)) #bool

"""
Lists are ordered and mutable collections used to store multiple items in a single variable
"""
e = [1,2,3]
print(type(e)) #list 
# Additional kuro - Elements in a list can be of different Data Types and are accessed using indexing.
# jastae
b = ["Pri", "For", "Don", 4, 5]
print(b[3]) # 4 print hune
print(b[-3]) # Pri print hune , minus garda paxadi bata counting suru hune 

"""
Tuple - Tuples are ordered and immutable collections
 used to store multiple items in a single variable. 

"""
t1 = (1,)
print(type(t1)) # tuple

"""
 Once created, tuple elements cannot be modified But are Accessed using Indexing.

Note: A tuple with a single element must include a trailing comma, otherwise 
Python treats it as a normal value instead of a tuple.

"""
t2 = ('Pri', 'For', 'Bhatt', 1, 2)
print(t2[3]) # 1 print hune
print(t2[-3]) # For print hune

"""
Boolean Data Type - Boolean data type represents one of
 two values: True or False. It is mainly used in conditions 
 and comparisons and is represented by the bool class.
"""
print(type(True)) # bool
print(type(False)) #bool

A=True
print(type(A)) #bool

"""
Set Data Type:
Sets are unordered and mutable collections used to store unique elements. 

"""
s1 = {"a", "a", "b", "c", "b"} # {'a', 'c', 'b'} will be print
print(s1)
print(type(s1)) #set

#Since sets are unordered, elements cannot be accessed using 
# indexing. Elements are usually accessed by iterating through the set using a loop As

s2 = {"Bhatani", "Bhatt", "Bhatani"}
for i in s2:
    print(i) #by doing this only prints Bhatani Bhatt

"""
Dictionary Data Type - Dictionaries are used to store data in key:value pairs. 
Each key in a dictionary must be unique and values are accessed 
using their keys with square brackets [] or get() method.

Note: Dictionary keys are case sensitive, 
the same name but different cases of Key will be treated distinctly. 
"""
d = {1: 'Pri', 2: 'For', 3: 'Bhatani'}
print(d[1])    # Pri will print
print(d.get(2)) # For will display now