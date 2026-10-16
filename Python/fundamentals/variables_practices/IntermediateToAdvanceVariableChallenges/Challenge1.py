"""Challenge 6: Server configuration

Task: Create variables for a server hostname, IP address, port, and status. 
Print a configuration report.

Hint 1:
Think about which values are text and which are numbers. For example, a hostname is text, 
while a port can be an integer.

Hint 2:
Give each variable a meaningful name, then use f-strings to print a report with labels.
Extra challenge: Align the labels so the report looks professional.
"""
#My solution:

#Here Defining Server Configuration Variables withh appropriate data types

hostname= "web-server-01" #hostname ->(points to) a string, e.g., "web-server-01"
IP_Address = "192.168.1.100" #IP_Address -> a string, e.g., "192.168.1.100" cuz
# (note: it's stored as text, not a number — cuz multiple dots aren't valid in floats!)
port=8080 #port variable points to a integer, e.g., 8080
status= "online" #Status ->a string like "online" or "offline" (or a boolean True/False you 
#want to practice booleans)

#Now Displaying the Server Configuration Report with some alignment that i can think
print("========SERVER CONFIGURATION REPORT========")

print(f"Hostname is :{hostname}") 
print(f"IP Address is :{IP_Address}")
print(f"Port is : {port}")
print(f"Status is :{status}")
print("===========================================")