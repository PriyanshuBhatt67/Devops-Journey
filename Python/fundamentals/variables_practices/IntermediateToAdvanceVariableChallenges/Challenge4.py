"""Challenge 9: Compare objects

Task: Create two separate lists containing the same elements, then compare them using == and is.

Hint 1
Create two lists independently, using the same values in each.
Hint 2
Remember:
- == checks whether the objects have equal values.
- is checks whether they are the very same object.
Predict the results before running your program.
"""

# we get Hint 1: Create two lists INDEPENDENTLY (two separate objects!)
list_a= [1, 2, 3]
list_b = [1, 2, 3]

# --- My predictions (writing these BEFORE running!) --
# list_a == list_b  -> True  (same values)
# list_a is list_b  -> False (different objects in memory)

print("Values are equal (==)  :", list_a == list_b)
print("Same object (is)       :", list_a is list_b)

# Extra: prove they're different objects with id()
print("\n--- Memory IDs ---")
print("Memory id of list_a    :", id(list_a))
print("Memory id of list_b    :", id(list_b))

# Extra: show the contrast — make both names point to the SAME object
list_c = list_a   # NOT a copy — just alias(another name) for the same list!
print("\nAfter list_c = list_a:")
print("Values are equal (==)  :", list_a == list_c)
print("Same object (is)       :", list_a is list_c)