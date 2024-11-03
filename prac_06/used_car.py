from prac_06.car import Car


def main():
    """Demonstration of using the Car class with different cars and driving scenarios."""
    sporty_car = Car("Sporty", 180)
    
    sporty_car.drive(45)
    
    print(f"Remaining fuel in {sporty_car.name}: {sporty_car.fuel} units")
    
    print(sporty_car)

    luxury_car = Car("Luxury", 100)
    
    luxury_car.add_fuel(30)
    
    print(f"Fuel after refueling {luxury_car.name}: {luxury_car.fuel} units")
    
    luxury_car.drive(120)
    
    print(luxury_car)

    luxury_car.drive(10)
    print(f"After another short trip, {luxury_car.name}'s status is: {luxury_car}")

main()
