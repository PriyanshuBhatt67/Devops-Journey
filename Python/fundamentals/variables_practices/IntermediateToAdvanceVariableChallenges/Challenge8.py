"""The Variable Rotation Puzzle

you will practice                                                                                                                        You'll practice
Reassignment order and why sequence matters.

You are given three variables:

a = 10
b = 20
c = 30

Rotate their values so that:
• a takes b's value
• b takes c's value
• c takes a's ORIGINAL value

After the rotation, printing a, b, c should give: 20 30 10                                                                                         Rules:
• Do it in as few lines as possible.
• Do NOT hardcode 10, 20, or 30 after the initial setup.

In a comment, explain why the ORDER of your assignments matters — what 
would happen to a's original value if you overwrote it first?
"""
#My Solution is :
a = 10
b = 20
c = 30

# --- The rotation ---
a, b, c = b, c, a   # one line, no hardcoding, no temp variable!

print(a, b, c)      # printing final rotated value as 20 30 10 

# --- Why order matters (comment as required by the challenge) ---
# The tuple(tuple vaneko immutable object ho) unpacking above works because Python evaluates ALL the values
# on the right-hand side (b, c, a) BEFORE making any assignments.
#
# If instead we overwrote 'a' FIRST:
#     a = b        # a = 20, and the original 10 is DESTROYED
#     b = c        # b = 30
#     c = a        # c = 20  (a's original 10 is gone — we get a's NEW value!)
#
# By overwriting a first, we lose its original value with no way to recover it — 
# that's why we must save/read it before any assignment happens.