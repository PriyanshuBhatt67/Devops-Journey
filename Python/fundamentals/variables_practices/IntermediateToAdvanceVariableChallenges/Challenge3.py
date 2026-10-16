"""
Challenge 8: Shared mutable reference

Task: Predict both lists after this code runs.

A = [1, 2]
b = A
b.append(3)
print(A)
print(b)

Hint 1
Draw a simple diagram: two variable names pointing to the same list object.
Hint 2
b.append(3) modifies the existing list. It does not assign a new list to b.
Key concept: Aliasing and mutation.

"""
A=[1,2] # Here by doing this, Python creates a list object containing 1 and 2 in memory, and 
#binds the name   A       as a reference to that object

b = A # here we copies the reference (the memory location address) from a to b    Or can be said as
#here We Copy reference address [the memory location], so   b   points to the same object as   A
b.append(3)#by doing this Adding/Appending to b but also changes A, since they share the same list  & 
#List is Mutable Object which means we can make changes
print(A) # Output would be [1,2,3]
print(b) #Output Would be same as A
