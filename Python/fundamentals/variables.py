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
# C wa C++ vako vaye Aile std::string name = "Priyanshu";  lekhnu parthyo String ko Data Type lai
#  declare garnu parthyo but Python vayekole haami lai jarurat hudaina 

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
Value lai Feri(Re) Assign gareko. Python Interpreter based language honi
ho tesaile jastae yaha haami le score naam ko variable maa 10 value store garyau ni 
& print vitra ni raakhau print garna ko lagi;tara
ani arko line maa same score naam ko variable maa arko value jastae 20 store garyau ni; 
20 store garepaxi tesko arko line maa haami le score naam ko variable lai ajhae print vitra
raakhyau ni; ho yaha Output Nikaalda ke hune vayo ki suru ko line maa
 tw 10 print hune ho cuz suru maa store naam ko variable vitra 10 value haalya xau but
Output ko second line maa 20 print hune Kina vane haami le aafno code maa 3rd line maa
score naam ko variable ko value lai ReAssign(feri kunae value raakheko) gareka xau
 and python interpreter le line by line check garne vayekole aafno suru ko line ko output
 10 aayo and arko 20
"""
score = 10
print(score)

score = 20
print(score)

"""
Multiple Assignment in Python-
What it means: 
Multiple assignment allows us to assign values to multiple variables 
simultaneously in a single line of code(nepali maa simplu yesto bujhda ni hunxa ki 
dherai values assign garna sakinxa ekae line maa). Instead of writing separate lines 
for every single variable, Python matches the values on the right side 
to the variables on the left side based on their positions.
"""

# 1. Basic Multiple Assignment
# Assigning three variables in one single line

x, y, z = 10, 20, 30
print(x,y,z)  # Output:10 20 30
"""yadi yesh maathi ko example multiple assignment use nagarera singlely value assign gareko
vaye our code would be lengthy like 
x=10
y=20
z=30
print(x,y,z) #output aaune
Ho yesari gareko vaye Code Lengthy hune thiyo; thats why we used Multiple Assignment technique in
maathi ko code
"""
#Another Example in Multiple Assignment is 
host,port,ssl = "priyanshu.com",443,True
print(host) # priyanshu.com print hune ho
print(port) # 443 print hune ho

# 2. Real-world example (Storing basic server or user data)
# Matching items position by position: name -> "Server-01", port -> 80, status -> True
server_name, port_number, is_online = "Server-01", 80, True

print(f"Server: {server_name}, Port: {port_number}, Online: {is_online}") 

""" yesh maathi ko example maa maile print vitra suru maa f lagayera paxi 2 ota
double quotes ko vitra na raakhera    just print paxi 2 ota double quotes vitra raakhya vaye
hamro Output would be                                   Server: {server_name} 
but f lagayeko kaaran hamro output will print           Server: Server-01

Basically in Python putting f before double quotation marks stands for 
Format (or f-string Or Formatted String Literal).    """


# 3. Swapping values easily with (no temp/temporary variables needed)
# In Python, you don't need a temporary variable to swap values!

apple_count = 5
orange_count = 10

print(f"Before swap -> Apples: {apple_count}, Oranges: {orange_count}")

# Now we Swap values instantly using multiple assignment
apple_count, orange_count = orange_count, apple_count

print(f"After swap  -> Apples: {apple_count}, Oranges: {orange_count}")

#Basic example of Multiple Assignment is 
a, b = 10, 20
a, b = b, a
print(a, b)  # aba output maa a=20 and b=10 vayo , easily swapped the values

# 4. Variables reference objects

"""In Python, a variable is not a box that holds data — it's a 
 name tag (reference) attached to an object in memory.
 OR 
 can be said as
 In Python, a variable does not store the value itself.

It stores a reference (a pointer / memory address) to an object. which as be  shown as

variable  variable  ──>  object in memory  object in memory
"""
# when we write 
x = 10
#python does 2 things - 
# i)Creates an object(which is integer object here)   10    in memory
# ii)Makes the name   x    point to that object

# 1) Now Basic Variable Reference Example:

A=100 #object lives in memory; 100 will live in memory
b=A # here b      now points to the same integer object(which is 100 here) as             A does
print(A) #100 print hune
print(b) #yesma ni 100 print hune
print(id(A))#yaha e.g 140712345678 dekhayo vane b ko ni same dekhaune ho cuz memory address dekhaune yesle
print(id(b))# same memory address dekhaune.  id of v cuz    same id(as A)   point to(Or -->) same object 10
print(A is b)#Output would be   True   cuz both points to same object(which is 100 here)
# id() shows the memory address of object
#if 2 variables have same id, they refer(points to) to the same object

#This example maa totally clearing doubt for How to references

x = [1, 2, 3]
y = x
z = [1, 2, 3]          # new list with same values

print(x is y)          # True  (same object)
print(x is z)          # False (different objects vayekole)
print(x == z)          # True  (same values)
print(id(x), id(y), id(z)) #Memory Address haru print hune hun, baaki yo related bataisake Ma Priyanshu le

#Now Another question will come in mind that why Variable reference is also important
#in order to understand ,let us see thhe another example

A=[1,2,3] # here the list [1,2,3] is object, list is example of mutable object
b=A
b.append(4) # append means adding
print(A) # Although we Append in   b  but when print A then got also change in A,Output : [1,2,3,4]
# Here Both names point to one list, so changing through b affects A.

#Another example is 
a = [1, 2, 3]
b = a

b.append(4)

print("a:", a)
print("b:", b)
print("Same object:", a is b)

#2)Interesting thing is Re-assignment creates a new reference , means that

""" when you assign a new value to an existing variable, you are changing which memory address 
that variable points to, rather than modifying the data inside the original memory address
Nepali maa matlab ki code maa kunae euta variable lai suru maa euta value
 diyera tesko id print garyau vane #memory address tw farak dekhaune ho 
 & tei code maa tyo same variable lai different value diyera
#print garda different memory address dekhaune ho cuz reality maa yei vayeko hunxa"""

#Example is

A=30
print(id(A))
A=20
print(id(A))