"""Challenge 3 : Valid variable names
# Identify which are valid: server_name, 2servers, serverIP, class, app_version, my-name. 
# Explain why in the comment. 
"""

#My solution here:

server_name = "1.2.3" # valid(cuz underscore symbole in between )

#2servers= "1.2.3" #invalid(cuz Python variable names cannot start with a digit),remove # in code to see error

serverIP="1.3.4" # t contains only letters, and there are no spaces or special symbols,
#making it completely valid (though following convention, it's better written as server_ip).

#class = server_name #Invalid cuz 
#class is a reserved keyword in Python (used to create classes for Object-Oriented Programming).
#  Python will throw a SyntaxError if you try to use a keyword like class, def, if, or for as
#  a variable name.

#my-name="priyanshu" #invalid cuz hypeny(-) in variable is treated as minu by python, remove # in code to see error