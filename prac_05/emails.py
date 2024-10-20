"""
CP1404/CP5632 Practical  
Email to Name Dictionary  
Estimate: 30 minutes  
Actual time: [Fill in your time here]  
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        guessed_name = extract_name_from_email(email)
        is_correct = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()

        if is_correct not in ("", "y"):
            name = input("Name: ")
        else:
            name = guessed_name

        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    prefix = email.split('@')[0]  
    parts = prefix.split('.')  
    guessed_name = " ".join(parts).title()  
    return guessed_name

main()
