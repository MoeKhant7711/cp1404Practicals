import random

random_integer = random.randint(5, 20)  # Line 1
print(f"Random integer between 5 and 20: {random_integer}")

random_range = random.randrange(3, 10, 2)  # Line 2
print(f"Random integer between 3 and 10 (step 2): {random_range}")

random_float = random.uniform(2.5, 5.5)  # Line 3
print(f"Random float between 2.5 and 5.5: {random_float}")

# What did you see on line 1?
# The smallest number could have been 5, and the largest could have been 20.

# What did you see on line 2?
# The smallest number could have been 3, and the largest could have been 9.
# No, line 2 could not produce a 4 because the step size is 2.

# What did you see on line 3?
# The smallest number could have been 2.5, and the largest could have been 5.5.

# Task: Generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)  # Example: 42
