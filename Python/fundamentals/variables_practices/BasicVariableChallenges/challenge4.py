"""Challenge 4: Update a counter
Task: Start with requests = 100, increase it by 25, then decrease it by 10.
Hint 1
Start with: requests = 100
Hint 2
Python has augmented assignment operators:
Instead of writing x = x + 5, you can use the x += 5. Both have same meaning
;writing x += 5 adds to the current value.
Ani Instead of writing x =x-5, we can use x -=5
;writing x -=5 subtracts from the current value.
Try applying both operators in the required order.
Your goal: Predict the final value before running the program."""

# My Solution :
requests = 100
#our goal is to prict final value, so here
requests += 25 # here variable named requests value becomes 125 after increasing by 25
requests -=10 # the updated value is now decreased by 10 , so becomes 115
# since my goal is to predict final value before running program,so my answer is 115
#to verify it Lets print the value by running this program
print(requests)
