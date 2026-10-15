"""Challenge 3 : Valid variable names
# Identify which are valid: server_name, 2servers, serverIP, class, app_version, my-name. 
# Explain why in the comment. 
"""

#My solution here:

server_name = "1.2.3" # valid(cuz underscore symbole in between )
#2servers= "1.2.3" #invalid(cuz variables naming rules doesn't allows numbers in staring),remove # in code to see error
serverIP="1.3.4" # no space in between
class saurav: server_name #valid cuz followed rules
app_version = "3.45.5" # again followed rules
#my-name="priyanshu" #invalid cuz hypeny(-) in variable is treated as minu by python, remove # in code to see error