"""  Challenge 5: Predict reassignment
Task: What is printed at the end?

status = "starting"
status = "running"
print(status)


Hint 1"
The second assignment binds status to a new string value.
Hint 2:
Since print() is called only after both assignments, ask yourself: which value 
is associated with status at that moment?


Your goal: Predict the output and explain why "starting" isn't printed.

"""
#My Solution

status ="starting"
status = "running"
#the ouput will print  running  cuz python is interpreter type language and we have reassigned
#our value "running" to the variable named status and the print the variable named status
#so that our output will come runnning
print(status)