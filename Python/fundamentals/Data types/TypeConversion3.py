"""
Mad Libs Story Generator
You'll practice
f-strings, and using a number as both text and math
Ask the user for 5 inputs: a name, an animal, a number, a food, and a city. Then weave them into a funny paragraph using an f-string.

The number must be used TWICE: once as plain text in the story, and once inside a calculation that also appears in the story.

Example:

Enter a name: Aisha
Enter an animal: panda
Enter a number: 3
Enter a food: samosa
Enter a city: Delhi

One day in Delhi, Aisha met a talking panda.
The panda ate 3 samosas... then asked for 3 * 2 = 6 more!

"""


name = input("Enter a name: ")
animal = input("Enter an animal: ")
number = int(input("Enter a number: "))
food = input("Enter a food: ")
city = input("Enter a city: ")

story = f"""One day in {city}, {name} met a talking {animal}.
The {animal} ate {number} {food}s... then asked for {number} * 2 = {number * 2} more!
{name} laughed so hard that even the {animal} joined in."""

print(story)

#OR

def mad_libs_generator():
    # 1. Collect inputs from the user
    name = input("Enter a name: ").strip()
    animal = input("Enter an animal: ").strip()

    # Convert number input to integer or float for mathematical operations
    number_input = input("Enter a number: ").strip()
    number = int(number_input)

    food = input("Enter a food: ").strip()
    city = input("Enter a city: ").strip()

    print("\n--- Here is your Mad Libs Story! ---\n")

    # 2. Weave inputs into a story using f-strings
    # 'number' is used as plain text ({number}) and in math ({number * 2})
    story = (
        f"One day in {city}, {name} met a talking {animal}.\n"
        f"The {animal} ate {number} {food}s... then asked for {number * 2} more!"
    )

    print(story)


if __name__ == "__main__":
    mad_libs_generator()
