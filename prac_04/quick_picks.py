import random

MIN_NUMBER = 1  
MAX_NUMBER = 45
NUM_PICKS = 6

quick_pick_count = int(input("How many quick picks would you like? "))  

for _ in range(quick_pick_count):
    selected_numbers = []  
    while len(selected_numbers) < NUM_PICKS:  
        random_pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_pick not in selected_numbers:
            selected_numbers.append(random_pick)
    selected_numbers.sort()
    print(" ".join(f"{number:2}" for number in selected_numbers)) 
