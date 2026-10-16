"""Challenge 10: Keep the old value

Task: Store an application's current version in old_version, update 
current_version, and print both values.
Hint 1:
Start with two variables representing the same initial version.
Hint 2:
Change only current_version. Don't update old_version.
Key concept: Two variable names can refer to immutable string values independently.
"""

# Step 1: Both start at the same initial version OR Both variables start with the same initial version ni vanna sakinxa
old_version = "1.0"
current_version = "1.0"

print("Before update:")
print(f"Old version     : {old_version}")
print(f"Current version : {current_version}")

# Step 2: Update ONLY current_version (old_version stays as-is)
current_version = "2.0"

print("\nAfter update:")
print(f"Old version     : {old_version}")      # still "1.0" 
print(f"Current version : {current_version}")  # aba "2.0" hune