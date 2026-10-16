"""Challenge 7: Assignment prediction
Task: Predict the values of a and b without running the code.

a = 5
b = a
a = 9
print(a)
print(b)

Hint 1:
When Python executes b = a, ask yourself: does b become permanently connected to the variable name a, or does it get assigned the current value/object that a refers to?
Hint 2:
Trace each line in order. After the final assignment, which name was reassigned?
Key concept: Assignment and rebinding. """
a=5
b=a
a=9
print(a)#9 will print
print(b)#5 will print