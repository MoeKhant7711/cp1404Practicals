from guitar import Guitar

def main():
    """Manage a collection of guitars."""
    print("My guitars!")
    guitars = []

    while True:
        name = input("Name: ")
        if not name:
            break  # Exit the loop if the user enters a blank name

        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20}, worth ${guitar.cost:10,.2f}{vintage_string}")

main()
