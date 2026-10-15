"""Imagine you have a box in which you store something.you write a label on that box so you can 
identify what's inside. ho yesari  nae bujhna sakinxa ki A variable works similarly like this example.
Variable is wastab maa euta Name ho that refers(points to) to a  value in our program
OR 
A variable is a name that stores data in memory.
OR
yesari ni bujhna sakinxa ki A Variable is a Named Container or Label used to store
Data Value in Computer memory.
Or
 variable is a named container that stores a value in memory. In Python haami le can create
   a variable simply by
assigning a value to a name using the = operator

OR 

just simply yesari ni bujhna sakinxa ki 
Variable is essentially a name assigned to a value
"""
# Basic Syntax is 

# Variable_Name=Value

# EK Main kura Bujhnu parne ki 
""" In Python we don't declare the Data Type/Type of Variable in
 Python(this Feature is called Dynamic Typing) """
#Python Automatically Detects the DataType based on the Value Assigned to Variable
# C & C++ programming languages xan ni; tesma yo Dynamic Typying wala feature hudaina
#Jastae example is
name = "Priyanshu" # haami lai yaha data type declare garnu parena,by the way string manxa python le yeslai
# C wa C++ vako vaye Aile std::string name = "Priyanshu";  lekhnu parthyo String ko Data Type lai declare garnu parthyo but Python vayekole haami lai jarurat hudaina 

print(name) # yo statement paxi 'Priyanshu' Print hunexa

""" 
 Python Variable Naming Rules

• Must start with: A letter (a-z, A-Z) or an underscore (_). It cannot start with a number.
• Allowed characters: Only letters, digits (0-9), and underscores (_). No spaces or symbols(tesma Hypen which is - , ni parxa So Hypen ni Use nagarne cuz Error aauna sakxa Hypen Use garyo vane).
• Case-Sensitive: user_name and User_Name are two completely different variables.
• No Keywords: Cannot use reserved Python words like if, for, while, class, or def.
• PEP 8 Convention: Yo chae recommended styling ko lagi ho; yesma We should 
 Use snake_case (all lowercase words separated by underscores) for making hamro code lai clean and
   readable code jasto

 Yo Rules Follow naGaryo vane Error aaune xa
"""
# Naming Variable Rules lai bujhna lai kei VALID EXAMPLES raakheko ni xu- 
user_name = "Priyanshu"       # Good & Valid(Standard snake_case)
_Server_Priyanshu= "10.0.0.1"   # Valid (Starts with a leading underscore)
server2_port = 22         # Valid (Contains a digit inside and not in starting)

#So now if we print these then we will not get error cuz we have followed the Variable Naming Rules
print(user_name)
print(_Server_Priyanshu)
print(server2_port)
# Example of INVALID name, here Python reads this as "user minus name"
# Have to remove Comment in this line for seeing error for          user-name = "Priyanshu" 


""" 1. Variable assignment( wa Variable maa value Assign garne) -kaam 
maathi ko example maa ni assign gariyo;  but with more examples lai tala herda hunxa """
name = "Priyanshu"
age = 21
is_learning_devops = True
University = "Farwestern"
print(name)
print(age)
print(is_learning_devops)
print(University)
"""2. Variable ReAssignment - Yo ni easy ho . Variable ReAssignment vanna le is
"""
score = 10
print(score)

score = 20
print(score)
