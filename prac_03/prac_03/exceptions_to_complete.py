"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: this line marks the input as valid and breaks the loop
    except ValueError:  # TODO - catch ValueError when the input is not a valid integer
        print("Please enter a valid integer.")
print("Valid result is:", result)


