"""
CP1404 Assignment 1 - Travel Tracker
Name: Moe Khant Zaw
Date started: 18.10.2024
GitHub URL:
"""

import random

FILENAME = 'places.csv'
VISITED = 'v'
UNVISITED = 'n'


def main():
    """Main function to run the Travel Tracker."""
    print("Travel Tracker 1.0 - by Moe Khant Zaw")
    places = load_places(FILENAME)
    if not places:  # Handle case where file is empty or not found
        print(f"No places loaded from {FILENAME}. Exiting.")
        return
    print(f"{len(places)} places loaded from {FILENAME}")
    menu(places)
    save_places(FILENAME, places)
    print(f"{len(places)} places saved to {FILENAME}")
    print("Have a nice day :)")


def menu(places):
    """Display the menu and process user input."""
    while True:
        print("\nMenu:\nD - Display all places\nR - Recommend a random place"
              "\nA - Add a new place\nM - Mark a place as visited\nQ - Quit")
        choice = input(">>> ").strip().upper()
        if choice == 'D':
            display_places(places)
        elif choice == 'R':
            recommend_place(places)
        elif choice == 'A':
            add_place(places)
        elif choice == 'M':
            mark_place_as_visited(places)
        elif choice == 'Q':
            break
        else:
            print("Invalid menu choice")


def load_places(filename):
    places = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, country, priority, visited = line.strip().split(',')
                places.append([name, country, int(priority), visited])
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return places


def save_places(filename, places):
    with open(filename, 'w') as file:
        for place in places:
            file.write(f"{place[0]},{place[1]},{place[2]},{place[3]}\n")


def sort_criteria(place):
    return (place[3], place[2])


def display_places(places):
    places.sort(key=sort_criteria)
    unvisited_count = sum(1 for place in places if place[3] == UNVISITED)
    longest_name = max(len(place[0]) for place in places)
    longest_country = max(len(place[1]) for place in places)

    for i, place in enumerate(places, 1):
        visited_marker = '*' if place[3] == UNVISITED else ' '
        print(f"{visited_marker}{i}. {place[0]:<{longest_name}} in {place[1]:<{longest_country}} {place[2]}")

    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")


def recommend_place(places):
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No places left to visit!")
    else:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {place[0]} in {place[1]}?")


def add_place(places):
    """Add a new unvisited place."""
    name = input("Name: ").strip()
    while not name:
        print("Input cannot be blank")
        name = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Input cannot be blank")
        country = input("Country: ").strip()

    while True:
        try:
            priority = int(input("Priority: "))
            if priority > 0:
                break
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")

    places.append([name, country, priority, UNVISITED])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_place_as_visited(places):
    """Mark an unvisited place as visited."""
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No unvisited places")
        return

    display_places(places)

    while True:
        try:
            place_number = int(input("Enter the number of a place to mark as visited: "))
            if place_number < 1 or place_number > len(places):
                print("Invalid place number")
            else:
                place = places[place_number - 1]
                if place[3] == VISITED:
                    print(f"You have already visited {place[0]}")
                else:
                    place[3] = VISITED
                    print(f"{place[0]} in {place[1]} visited!")
                    break
        except ValueError:
            print("Invalid input; enter a valid number")


main()