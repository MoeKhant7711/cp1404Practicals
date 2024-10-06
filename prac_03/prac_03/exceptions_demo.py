def get_user_input(prompt):
    """Function to get a valid integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Input must be a valid integer. Please try again.")

def divide_numbers(numerator, denominator):
    """Function to perform division and handle ZeroDivisionError."""
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero!")

def main():
    """Main function to run the program."""
    numerator = get_user_input("Enter the numerator: ")
    denominator = get_user_input("Enter the denominator: ")

    try:
        fraction = divide_numbers(numerator, denominator)
        print(f"The result of {numerator} divided by {denominator} is: {fraction}")
    except ZeroDivisionError as e:
        print(e)

    print("Finished.")

if __name__ == "__main__":
    main()

# Questions
# 1. When will a ValueError occur?
# A ValueError will occur when the input value cannot be converted to an integer, such as when the user inputs a non-numeric string.
# 2. When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur if the user inputs 0 as the denominator when performing division.
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, I changed the code to prompt the user for valid inputs repeatedly until valid integers are provided.
