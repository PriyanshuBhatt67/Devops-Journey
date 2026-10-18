"""
Number Analyzer

You'll practice

Comparison and modulo operators

Take two numbers from the user and report on their relationship.



Print:

Which number is larger (or whether they are equal)
The remainder when the larger is divided by the smaller
Whether both are even, both odd, or mixed


Example:

Enter first number: 12

Enter second number: 8

Larger: 12

Remainder of 12 / 8: 4

Both even

Hint: the modulo operator % gives you the remainder, and a number is even when n % 2 == 0. 

"""

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

# 1. Which is larger?
if first > second:
    larger = first
    smaller = second
    print(f"Larger: {first}")
elif second > first:
    larger = second
    smaller = first
    print(f"Larger: {second}")
else:
    larger = first
    smaller = second   # equal — either works
    print("Both numbers are equal")

# 2. Remainder of larger / smaller (guard against division by zero)
if smaller != 0:
    remainder = larger % smaller
    print(f"Remainder of {larger} / {smaller}: {remainder}")
else:
    print("Remainder: undefined (division by zero)")

# 3. Even/odd classification
first_even = first % 2 == 0
second_even = second % 2 == 0

if first_even and second_even:
    print("Both even")
elif not first_even and not second_even:
    print("Both odd")
else:
    print("Mixed")


    # OR


def analyze_numbers():
    # 1. Take two numbers from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # 2. Determine which number is larger (or if they are equal)
    if num1 > num2:
        print(f"Larger: {num1}")
        larger, smaller = num1, num2
    elif num2 > num1:
        print(f"Larger: {num2}")
        larger, smaller = num2, num1
    else:
        print("Both numbers are equal.")
        larger, smaller = num1, num2

    # 3. Calculate the remainder when the larger is divided by the smaller
    if smaller != 0:
        remainder = larger % smaller
        print(f"Remainder of {larger} / {smaller}: {remainder}")
    else:
        print("Division by zero is not possible.")

    # 4. Check if both are even, both odd, or mixed
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Both even")
    elif num1 % 2 != 0 and num2 % 2 != 0:
        print("Both odd")
    else:
        print("Mixed")


if __name__ == "__main__":
    analyze_numbers()