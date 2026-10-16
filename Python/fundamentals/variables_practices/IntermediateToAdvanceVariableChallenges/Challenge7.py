#Challenge 12:The Unit Converter
"""
You'll practice
Deriving many values from a single source variable
Store a distance in kilometers in one variable, then convert it into several units, each held in its own variable.

From km, compute:
• miles       = km × 0.621
• meters      = km × 1000
• centimeters = km × 100000
• feet        = km × 3280.84

Print a formatted summary.

Example (km = 5):

5 km equals:
  Miles:       3.105
  Meters:      5000
  Centimeters: 500000
  Feet:        16404.2

Change km at the top just once and confirm every line updates automatically.
 Nothing else should need editing.

"""
"""Challenge: The Unit Converter

Task: Store a distance in kilometers in one variable, then convert it 
into several units, each held in its own variable.
"""

# Define the source variable at the top (change this to test!)
km = 5

# Computing all other units from the single km variable
miles = km * 0.621
meters = km * 1000
centimeters = km * 100000
feet = km * 3280.84

# Now Printing a formatted summary
print(f"{km} km equals:")
print(f"  Miles:       {miles}")
print(f"  Meters:      {meters}")
print(f"  Centimeters: {centimeters}")
print(f"  Feet:        {feet}")