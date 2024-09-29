import random

def main():
    user_score = int(input("Enter your score: "))
    user_result = get_score_result(user_score)
    print(f"Your result: {user_result}")

    random_score = random.randint(0, 100)
    random_result = get_score_result(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
