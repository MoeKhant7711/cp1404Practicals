def main():
    """Main function to run both parts of the program."""
    number_information()  
    security_checker()   

def number_information():
    """Collects 5 numbers, stores them in a list, and displays various statistics."""
    numbers = []  

    for i in range(5):
        number = float(input(f"Number {i + 1}: "))  
        numbers.append(number)  

    # Display information about the numbers
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

def security_checker():
    """Checks if the entered username is in the list of authorised users."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 
        'Command', 'ExecState', 'InteractiveConsole', 
        'InterpreterInterface', 'StartServer', 'bob'
    ]

    user = input("Enter your username: ")
    if user in usernames:
        print("Access granted")
    else:
        print("Access denied")
main()
